from src.templates.controllers import create_trainee, get_all_trainees, get_trainee_by_id, update_trainee, delete_trainee

from src.models.model import traineeModel, traineeUpdateModel
from fastapi import FastAPI, HTTPException, status

app = FastAPI (
    title="Gestion de datos de aprendices",
    description="API para gestionar los datos de los aprendices",
    version="1.0.0",
)
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de gestión de aprendices"}