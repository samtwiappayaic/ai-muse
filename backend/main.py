#uvicorn main:app
#uvicorn main:app --reload
# source venv/bin/activate    

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai
import asyncio

#Custom Function Imports
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

#Initiate app
app = FastAPI()

# CORS - Origins 
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=True,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

#Check health
@app.get("/health")
async def check_health():
    return {"message": "Healthy"}

# Reset messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}

#Get audio
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    #Save file chunk from frontend
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_chunk = open(file.filename, "rb")

    #Decode audio
    transcript = convert_audio_to_text(audio_chunk)
    
    #Guard: Ensure message decoded
    if not transcript:
        return HTTPException(status_code=400, detail="Failed to decode audio")
        
    def transcriptions_generator():
        yield f"data: {transcript}"
    

    return StreamingResponse(transcriptions_generator(), media_type="text/event-stream")


