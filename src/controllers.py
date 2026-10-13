from bson import ObjectId
from src.models.database import collection
from src.models.model import traineeModel, traineeUpdateModel
#el helper es una funcion que ayuda a convertir los datos de un objeto en un diccionario para poder ser manipulados y retornados en formato JSON.
def helper_trainee(trainee) -> dict: 
    return {
        "id": str(trainee["_id"]),
        "document": trainee["document"],
        "firstname": trainee["firstname"],
        "lastname": trainee["lastname"],
        "email": trainee["email"],
        "age": trainee["age"],
        "program": trainee["program"],
        "record_number": trainee["record_number"]
    }