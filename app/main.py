from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Servidor Inicializado": "Hola Mundo FastAPI a N8N"}

