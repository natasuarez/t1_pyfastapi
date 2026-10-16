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
    
    
def create_trainee(trainee: traineeModel):
    trainee_dict = trainee.model_dump()   #Es un método que convierte el objeto trainee en un diccionario.
    result = collection.insert_one(trainee_dict)  #Se inserta el diccionario
    new_trainee = collection.find_one({"_id": result.inserted_id})  #Se busca el objeto insertado por su id
    return helper_trainee(new_trainee)  #Se retorna el objeto convertido en diccionario mediante el helper

#Obtener todos los aprendices
def get_all_trainees():
    trainees = []
    for trainee in collection.find():
        trainees.append(helper_trainee(trainee))  #Se recorre la colección y se convierte cada objeto en diccionario mediante el helper
    return trainees  #Se retorna la lista de diccionarios
#Obtener datos del aprendiz por id 
def get_trainee_by_id(id: str):
    trainee = collection.find_one({"_id": ObjectId(id)})  #Se busca el objeto por su id
    if trainee:
        return helper_trainee(trainee)  #Se retorna el objeto convertido en diccionario mediante el helper
    return None #Si no se encuentra el objeto, se retorna None 

#Actualizar datos del aprendiz por id 
def update_trainee(id: str, trainee: traineeUpdateModel):
   data_update = {k: v for k, v in trainee.model_dump().items() if v is not None}  #Se crea un diccionario con los datos a actualizar
   if data_update:
       collection.update_one({"_id": ObjectId(id)}, {"$set": data_update})  #Se actualiza el objeto en la colección
       trainee_updated = collection.find_one({"_id": ObjectId(id)})  #Se busca el objeto actualizado por su id
       return helper_trainee(trainee_updated)  #Se retorna el objeto convertido en diccionario mediante el helper
   return None  #Si no se encuentra el objeto, se retorna None

#Eliminar datos del aprendiz por id
def delete_trainee(id: str):
    trainee = collection.find_one({"_id": ObjectId(id)})  #Se busca el objeto por su id
    if trainee:
        collection.delete_one({"_id": ObjectId(id)})  #Se elimina el objeto de la colección
        return True  #Se retorna True si se eliminó correctamente
    return False  #Si no se encuentra el objeto, se retorna False