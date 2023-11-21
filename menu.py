import os
import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("============================")
        print("    BIENVENIDO AL MANAGER   ")
        print("============================")
        print("[1]Listar cliente           ")
        print("[2]Buscar cliente           ")
        print("[3]Añadir cliente           ")
        print("[4]Modificar cliente        ")
        print("[5]Borrar cliente           ")
        print("[6]Cerrar cliente           ")
        print("============================")

        option = input("> ")
        helpers.limpiar_pantalla()

        if option == "1":
            print("Listado los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)
            
        elif option == "2":
            print("Buscando un clientes...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("cliente no encontrdo.")
            
        elif option == "3":
            print("Añadiendo un clientes...\n")

            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")
            
        elif option == "4":
            print("Modificando un clientes...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(
                    2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(
                    2, 30, f"Apellido(de 2 a 30 chars) [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")


        elif option == "5":
            print("Borrando un clientes...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            print("Cliente borrado correctamrnte.") if db.Clientes.borrar(
                dni) else print("cliente no encontrado.")
                
        elif option == "6":
            print("Saliento.....\n")
            break
    
        input("\nPresionar ENTER para continuar...")


        

        

         

