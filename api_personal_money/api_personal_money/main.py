from imp import reload
from typing import Optional
from fastapi import FastAPI
from pip import main

app = FastAPI()

cartoes = {
    1: {
        "cartoes_id": 1,
        "descricao": "NuBank",
        "bandeira": "Mastercard",
        "tipo": ["Débito", "Crédito"]
    }
}
@app.get("/cartoes")
async def get_cartoes():
    return cartoes

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        reload=True,
        host="127.0.0.1",
        port=8001
    )