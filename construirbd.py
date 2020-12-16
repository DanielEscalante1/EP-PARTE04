
#----------- ARCHIVOS TXT -----------------

print("\n***CLAVES***")
claves = open("claves.txt", "rt", encoding="utf8")
datos_claves = claves.read()
print(datos_claves)

print("\n***CoDIGOS***")
codigo = open("codigo.txt", "rt", encoding="utf8")
datos_codigo = codigo.read()
print(datos_codigo)


print("\n***NOMBRES***")
nombre = open("nombre.txt", "rt", encoding="utf8")
datos_nombre = nombre.read()
print(datos_nombre)


print("\n***PRECIOS***")
precio = open("precio.txt", "rt", encoding="utf8")
datos_precio = precio.read()
print(datos_precio)


print("\n***USUARIOS***")
usuarios = open("usuarios.txt", "rt", encoding="utf8")
datos_usuarios = usuarios.read()
print(datos_usuarios)


#-----------CREACIÓN DE BD -----------------
import sqlite3
conexion = sqlite3.connect("ventas.db")
conexion.close()
    

#-----------CREACIÓN DE TABLAS EN BD -----------------


conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
tabla_usuario = ("""CREATE TABLE USUARIO(
                     IDUSUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
                     USUARIO TEXT UNIQUE,
                     CLAVE TEXT)""")
tabla_producto = ("""CREATE TABLE PRODUCTO(
                     IDPRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE TEXT,
                     CODIGO TEXT,
                     PRECIO NUMBER )""")

cursor = conexion.cursor()
cursor.execute(tabla_usuario)
cursor.execute(tabla_producto)
conexion.close()


#-----------LEER E INSERTAR TABLA 01 -----------------

conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()

lista_usuario = datos_usuarios.split('\n')
lista_clave = datos_claves.split('\n')

for indice,valor in enumerate(zip(lista_usuario,lista_clave)):  
    print(valor[0],valor[1])
    cursor.execute("INSERT INTO USUARIO(USUARIO,CLAVE)VALUES('"+valor[0]+"','"+valor[1]+"')")

#CONFIRMAR CAMBIOS CON COMMIT
conexion.commit()
conexion.close()
    
#-----------LEER E INSERTAR TABLA 02 -----------------

conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
lista_nombre = datos_nombre.split('\n')
lista_codigo = datos_codigo.split('\n')
lista_precio = datos_precio.split('\n')

for indice,valor in enumerate(zip(lista_nombre,lista_codigo,lista_precio)):  
    print(valor[0],valor[1])
    cursor.execute("INSERT INTO PRODUCTO(NOMBRE,CODIGO,PRECIO)VALUES('"+valor[0]+"','"+valor[1]+"','"+valor[2]+"')")
   
conexion.commit()
conexion.close()


