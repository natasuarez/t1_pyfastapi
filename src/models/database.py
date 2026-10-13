from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

#Agregar la URI de conexión a la base de datos MongoDB
MONGO_URI = "mongodb+srv://natasuarezxx_db_user:Nps_1025656327@cluster0.zxzaki3.mongodb.net/?appName=Cluster0"

#Crear una instancia del cliente de MongoDB y asignar tiempo de espera para la selección del servidor
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
#Crear una instancia de la base de datos y la colección que se utilizará
db =client.dataap
collection = db.trainee

try:
    #Intentar obtener información del servidor para verificar la conexión
    client.server_info()
    client.admin.command('ping')
    print("Conexión exitosa a la base de datos MongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error al conectar a la base de datos MongoDB: {e}")
finally:
    #Cerrar la conexión al cliente de MongoDB
    client.close()