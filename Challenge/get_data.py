#Programa que consume los datos de un Endpoint expuesto y los almacena en una Base de datos
#Creador : John Alexander Pachón Pinzón
import requests
import pandas as pd
import hashlib
import json
from insert_data import insert_card, commit_db

#importar los datos de la URL
data = requests.get ('https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios')
data_cards = data.json()

#Obtener los encabezados de seguridad de la web
cab = data.headers ['Content-Type']
#print(cab)

#Convertir json a DataFrame para cifrar posteriormente
df = pd.DataFrame(data_cards)

# Convertir columna a cadena 
df['credit_card_num'] = df['credit_card_num'].astype(str)
df['credit_card_ccv'] = df['credit_card_ccv'].astype(str)
df['cuenta_numero'] = df['cuenta_numero'].astype(str)
df['direccion'] = df['direccion'].astype(str)
df['ip'] = df['ip'].astype(str)

# Aplicar la función hash a la columna 
df['credit_card_num'] = df['credit_card_num'].apply( lambda x: hashlib.sha256(x.encode()).hexdigest())
df['credit_card_ccv'] = df['credit_card_ccv'].apply( lambda x: hashlib.sha256(x.encode()).hexdigest())
df['cuenta_numero'] = df['cuenta_numero'].apply( lambda x: hashlib.sha256(x.encode()).hexdigest())
df['direccion'] = df['direccion'].apply( lambda x: hashlib.sha256(x.encode()).hexdigest())
df['ip'] = df['ip'].apply( lambda x: hashlib.sha256(x.encode()).hexdigest())

#Convertir el DF en 
Cifrado = df.to_dict('records')

#Ciclo para insertar los datos en la base de datos
for card in Cifrado:
  insert_card(card)
  #print(type(card))
  commit_db()

#cerrar la conexión de la base de datos
#shutdown()

