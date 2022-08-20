import pymysql

##Conexión a la Base de datos MySQL
db = pymysql.connect(host='cardsjp.ceyducckchrz.us-east-2.rds.amazonaws.com', user= 'challenge', passwd='voJiqAhA', db='Cards', cursorclass=pymysql.cursors.DictCursor)
cur = db.cursor()
cur.execute("""SELECT now()""")
cur.execute("SELECT VERSION()")
ver = cur.fetchone()
#print ("Database version : %s " % ver)

#Ver tablas creadas
cur.execute("Show tables;") 
myresult = cur.fetchall()
for x in myresult:
    y = x
    #print(x)

##Creación de tabla
if y == x:
    print("LA TABLA QUE ESTA INTENTANDO CREAR, YA EXISTE")
else:
  cur.execute("CREATE TABLE cards (fec_alta VARCHAR(255),\
                                user_name VARCHAR(255),\
                                codigo_zip VARCHAR(255),\
                                credit_card_num VARCHAR(255),\
                                credit_card_ccv VARCHAR(255),\
                                cuenta_numero VARCHAR(255),\
                                direccion VARCHAR(255),\
                                geo_latitud VARCHAR(255),\
                                geo_longitud VARCHAR(255),\
                                color_favorito VARCHAR(255),\
                                foto_dni VARCHAR(255),\
                                ip VARCHAR(255),\
                                auto VARCHAR(255),\
                                auto_modelo VARCHAR(255),\
                                auto_tipo VARCHAR(255),\
                                auto_color VARCHAR(255),\
                                cantidad_compras_realizadas VARCHAR(255),\
                                avatar VARCHAR(255),\
                                fec_birthday VARCHAR(255),\
                                id VARCHAR(255)       ) ")


#Función para insertar en la DB los datos recibidos del endpoint
def insert_card(card):
   cur.execute("INSERT INTO \
    cards (fec_alta, user_name, codigo_zip, credit_card_num, credit_card_ccv,\
         cuenta_numero, direccion, geo_latitud, geo_longitud, color_favorito,\
           foto_dni, ip, auto, auto_modelo, auto_tipo, auto_color, \
            cantidad_compras_realizadas,  avatar, fec_birthday, id) \
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
     (card["fec_alta"], card["user_name"], card["codigo_zip"], card["credit_card_num"],
      card["credit_card_ccv"], card["cuenta_numero"], card["direccion"], 
      card["geo_latitud"], card["geo_longitud"], card["color_favorito"],
      card["foto_dni"], card["ip"], card["auto"], card["auto_modelo"], 
      card["auto_tipo"], card["auto_color"], card["cantidad_compras_realizadas"],
      card["avatar"], card["fec_birthday"], card["id"])) 

#Commit para la actualización en la DB  
def commit_db():
  cur.connection.commit()

#Ver Cantidad de datos almacenados
#cur.execute("Select count(user_name) FROM Cards.cards")
#Consulta = cur.fetchall()
#for x in Consulta:
#  print(x) 
  
