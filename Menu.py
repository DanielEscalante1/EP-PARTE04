# -*- coding: utf-8 -*-
import os
import sqlite3
# Para conectarnos a la BD
def menuPrincipal():
            continuar=True
            while(continuar):
                opcionCorrecta=False
                while(not opcionCorrecta):
                    print("-------- MENU PRINCIPAL --------")
                    print("1. Listar")
                    print("2. Agregar")
                    print("3. Eliminar")
                    print("4. Modificar")
                    print("5. Salir")
                    opcion = int(input("Seleccione una opccion: "))
                
                    if opcion < 1 or opcion > 5:
                        print("OPCION INCORRECTA - VUELVA A INSERTAR UNA OPCION")
                        
                    else:
                        if opcion == 5:
                            print("CERRADO EXITOSAMENTE")
                            continuar=False
                            break
                        else:
                            opcionCorrecta=True
                            ejecutarOpcion(opcion)
      
def listar():
    
            conexion=sqlite3.connect("ventas.db")
            cursor=conexion.cursor()
            
            print("NOMBRE\t\t\t"+"PRECIO\t\t\t"+"CODIGO")
            cursor.execute("""select NOMBRE,PRECIO,CODIGO
                           from PRODUCTO
                           order by IDPRODUCTO""")
            
            productos=cursor.fetchall()
            
            for producto in productos:
                print(producto[0],producto[1],producto[2])
            conexion.close()
    
def agregar():
    
            import sqlite3
            conexion = sqlite3.connect("ventas.db")
            cursor = conexion.cursor()
                
            p = input("Ingrese Nombre: ")
            e = input("Ingrese Codigo: ")
            c = input("Ingrese Precio: ")
            
            cursor.execute('INSERT INTO PRODUCTO (NOMBRE, CODIGO, PRECIO) VALUES(?,?,?)',(p, e, c))
            
            conexion.commit()
            conexion.close() 
            print("PRODUCTO AGREGADO EXITOSAMENTE\n")   
      
def eliminar():
            codigo = int (input("ingrese codigo del producto: "))
            
            conexion=sqlite3.connect("ventas.db")
            cursor=conexion.cursor()
            consulta = (f"""DELETE FROM 
                              PRODUCTO
                              WHERE
                              CODIGO = {codigo}""")
            
            cursor.execute(consulta)
            conexion.commit()
            
            conexion.close()
            print("PRODUCTO ELIMINADO EXITOSAMENTE\n")
    
def modificar():
            conexion = sqlite3.connect("ventas.db")
            cursor = conexion.cursor()
            e = int(input("Codigo del PRODUCTO a modificar: "))
            p = input("Nuevo Nombre del PRODUCTO a modificar: ")
            c = input("Nuevo Precio del PRODUCTO a modificar: ")
            
            cursor.execute("UPDATE PRODUCTO SET NOMBRE = '%s', PRECIO = '%s' WHERE CODIGO = '%s'" %(p, c, e))
            conexion.commit()
            conexion.close()
            print("PRODUCTO ACTUALIZADO EXITOSAMENTE\n")

    
def error():
    print ("")
    input("No has ingresado ninguna opción correcta...\npulsa una tecla para continuar")
    
def ejecutarOpcion(opcion):

        if opcion == 1: #LISTAR
            listar()  

        elif opcion == 2: #AGREGAR
            agregar()
            
        elif opcion==3: #ELIMINAR
            eliminar()
            
        elif opcion == 4: #MODIFICAR
            modificar()

        else:
            error()
        

menuPrincipal()


