from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from config import settings
from api.routers import api_router

app = FastAPI(
    title = settings.PROJECT_NAME,
    version = settings.PROJECT_VERSION
)

origins = [
    'https://tutor-bot-phi.vercel.app',
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["GET", "POST", "PUT", "DELETE"],
    allow_headers = ["*"]
)

router = APIRouter()


# Datos del quiz en formato JSON
quiz_data = [
    {
        "question": "¿Cuál es el resultado de ejecutar el siguiente código en Java?",
        "options": [
            "a) Output: Hello World!",
            "b) Output: Hello",
            "c) Output: World!",
            "d) Output: Error"
        ],
        "answer": 0
    },
    {
        "question": "¿Qué tipo de variable existe en Java y puede tener cualquier valor entre entre dos valores definidos?",
        "options": [
            "a) Integer",
            "b) Float",
            "c) String",
            "d) Enum"
        ],
        "answer": 3
    },
    {
        "question": "¿Cuál es el método que se utiliza para arreglar un arreglo en Java?",
        "options": [
            "a) sort()",
            "b) reverse()",
            "c) shuffle()",
            "d) forEach()"
        ],
        "answer": 0
    },
    {
        "question": "¿Qué es un método en Java?",
        "options": [
            "a) Un conjunto de comandos para ejecutar en el terminal",
            "b) Un conjunto de sentencias para realizar una tarea",
            "c) Un block de código que se puede llamar varias veces",
            "d) Un ciclo iterativo"
        ],
        "answer": 2
    },
    {
        "question": "¿Qué es un booleano en Java?",
        "options": [
            "a) Un tipo de dato numérico",
            "b) Un tipo de dato de texto",
            "c) Un tipo de dato lógico",
            "d) Un tipo de dato de fecha"
        ],
        "answer": 2
    }
]
#Endpoint para obtener el quiz
@router.get("/quiz", response_model=List[dict])
async def get_quiz():
    return quiz_data


app.include_router(api_router, prefix='/api/v1')
app.include_router(router)