#Importar libreria de sql que contiene funciones de Base de datos en uso 
import sql 

#Crear la tabla 
sql.initDB()

#Menu principal 

def menu():
    while True:
        print("""======= BIBLIOTECA =======
        1. Agregar nuevo libro
        2. Actualizar información de un libro
        3. Eliminar libro existente
        4. Ver listado de libros
        5. Buscar libros
        6. Salir""")
        
        try:
            opcion = int(input("Seleccione una opcion 1-6: "))
        except ValueError:
            print("Ingrese un dato numerico.")

        #Opciones Agregar un libre
        if opcion == 1:
            t = input("Titulo: ")
            au = input("Autor: ")
            g = input("Genero: ")
            an = input("Año del libro: ") 
            e = int(input("Estado (1. Leido / 2.No leido): "))
            sql.AddLibro(t, au, g,an, e)

        #Actualizar un libro
        elif opcion == 2:
            listar = sql.ListLibros()

            if not listar:
                print("\n No hay resultados.\n")
                continue
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for l in listar:
                    estado = l["Estado_Lectura"]
                    if estado == 1:
                        estado = "Leido"
                    else:
                        estado = "No leido"
                    print(f"\nID: {l['_id']}\nTítulo: {l['Titulo']}\nAutor: {l['Autor']}\nGénero: {l['Genero']}\nAño: {l['Ano']}\nEstado: {estado}\n")
                    
            try:
                id = input("Ingrese el ID del libro a actualizar (puede copiar y pegar el id): ")
            except:
                print("ID invalido.")
                continue

            t = input("Nuevo titulo: ")
            au = input("Nuevo autor: ")
            g = input("Nuevo genero: ")
            an = input("Nuevo año del libro: ") 
            es = input("Nuevo estado (1. Leido / 2.No leido): ")

            sql.UpdateLibro(id, t, au, g,an, es)

        #Eliminar un libro
        elif opcion == 3:
            listar = sql.ListLibros()

            if not listar:
                print("\n No hay resultados.\n")
                continue
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for l in listar:
                    estado = l["Estado_Lectura"]
                    if estado == 1:
                        estado = "Leido"
                    else:
                        estado = "No leido"
                    print(f"\nID: {l['_id']}\nTítulo: {l['Titulo']}\nAutor: {l['Autor']}\nGénero: {l['Genero']}\nAño: {l['Ano']}\nEstado: {estado}\n")
                        
            try:
                id = input("Ingrese el ID del libro a eliminar: ") 
            except:
                print("ID invalido.")
                continue

            sql.DeleteLibro(id)

        #Listado de libros
        elif opcion == 4:
            listar = sql.ListLibros()
            if not listar:
                    print("\n No hay resultados.\n")
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for l in listar:
                    estado = l["Estado_Lectura"]

                    if estado == 1:
                        estado = "Leido"
                    else:
                        estado = "No leido"
                    print(f"\nID: {l['_id']}\nTítulo: {l['Titulo']}\nAutor: {l['Autor']}\nGénero: {l['Genero']}\nAño: {l['Ano']}\nEstado: {estado}\n")

        #Busqueda de libros    
        elif opcion == 5:
            print("\nBuscar por:")
            print("1. Título")
            print("2. Autor")
            print("3. Género")

            tipo = input("Seleccione opcion: ")

            if tipo == "1":
                valor = input("Ingrese título: ")
                resultados = sql.GetLibro("Titulo", valor)

            elif tipo == "2":
                valor = input("Ingrese autor: ")
                resultados = sql.GetLibro("Autor", valor)

            elif tipo == "3":
                valor = input("Ingrese género: ")
                resultados = sql.GetLibro("Genero", valor)

            else:
                print("Opción inválida.")
                continue

            if not resultados:
                    print("\n No hay resultados.\n")
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for l in resultados:
                    estado = l["Estado_Lectura"]
                    if estado == 1:
                        estado = "Leido"
                    else:
                        estado = "No leido"
                    print(f"\nID: {l['_id']}\nTítulo: {l['Titulo']}\nAutor: {l['Autor']}\nGénero: {l['Genero']}\nAño: {l['Ano']}\nEstado: {estado}\n")
                        
        elif opcion == 6:
            print("Hasta luego")
            break

        else:
            print("La opcion no existe, intente nuevamente.")

if __name__ == "__main__":
    menu()