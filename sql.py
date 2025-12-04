#Importar biblioteca de PyMongoDB
from pymongo import MongoClient
from bson.objectid import ObjectId

#Cadena de conexion de la bd
def conn():
    try:
        #cadena = Uri proveniente del cliente
        engine = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS = 3000)
        db = engine["libreriaDB"]
        return db
    except Exception as e:
        print("Error al conectar con la base de datos:", e)
        raise

def initDB():
    db = conn()
    if db is None:
        return

#Funciones para agregar, actualizar, eliminar, ver listado de libros y buscar libros 

def AddLibro(Titulo,Autor,Genero,Ano,Estado):
    db = conn()
    if db is None: 
        return 
    
    try:
        nuevo = {
        "Titulo": Titulo,
        "Autor": Autor,
        "Genero": Genero,
        "Ano": int(Ano),
        "Estado_Lectura": int(Estado)  # 1 leido, 0 no leido
    }

        db.libro.insert_one(nuevo)

        print("Libro Agregado.")

    except Exception as e:
        print("Error SQL:", e)


def UpdateLibro(id1, Titulo, Autor, Genero, Ano, Estado):
    db = conn()
    if db is None: 
        return     

    try:
        resultado = db.libro.update_one(
            {"_id": ObjectId(id1)},
            {"$set": {
                "Titulo": Titulo,
                "Autor": Autor,
                "Genero": Genero,
                "Ano": int(Ano),
                "Estado_Lectura": int(Estado)
            }}
        )
        print("libros actualizados:", resultado.modified_count)

    except Exception as e:
        print("Error al actualizar libro:", e)


def DeleteLibro(id1):
    db = conn()
    if db is None: 
        return     

    try:
        resultado = db.libro.delete_one({"_id": ObjectId(id1)})
        print("Libros eliminados:", resultado.deleted_count)
    except Exception as e:
        print("Error al eliminar libro:", e)


def ListLibros():
    db = conn()
    if db is None: 
        return  []
    
    return list(db.libro.find())


def GetLibro(campo,id):
    db = conn()
    if db is None: 
        return []
    
    query = {campo: {"$regex": id, "$options": "i"}}
    return list(db.libro.find(query))
