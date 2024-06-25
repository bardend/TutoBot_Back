from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import speech_recognition as sr 


from ai.groqconnetion import groqConnection

router = APIRouter()


class ModelRequest(BaseModel):
    question: str
    name: str


@router.post('/ask')
async def ask_question(req: ModelRequest):

    question = req.question
    name = req.name
    try:
        content = groqConnection.ask_groq(question, name)
        return {'res': content}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to ask to groq" + str(e))

@router.get('/mssg')
async def get_message():
    return {"message": "Out from backend"}

@router.get('/speech-to-text')
async def speech_to_text():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = listener.listen(source, phrase_time_limit=4)
            print("Reconociendo el audio...")
            audio_text = listener.recognize_google(audio, language="es-PE").lower()
            return {"transcript": audio_text}
    except sr.RequestError:
        raise HTTPException(status_code=500, detail="Servicio de reconocimiento de voz no disponible")
    except sr.UnknownValueError:
        raise HTTPException(status_code=400, detail="No se pudo entender el audio")
