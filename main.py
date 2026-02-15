print("Deploy nuevo con endpoint analizar activo")
print("Cambio nuevo")
print("Cambio nuevo2")


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextoInput(BaseModel):
    texto: str

@app.get("/")
def root():
    return {"mensaje": "Servidor Python activo 🚀"}

@app.post("/analizar")
def analizar(data: TextoInput):
    texto_recibido = data.texto
    return {
        "longitud_texto": len(texto_recibido),
        "preview": texto_recibido[:50]
    }
