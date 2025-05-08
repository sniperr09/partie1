from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

class Personnage(BaseModel):
    nom: str
    role: str

personnages = [
    Personnage(nom="Link", role="Héros d'Hyrule"),
    Personnage(nom="Samus Aran", role="Chasseuse de primes")
]

@app.get("/personnages", response_model=List[Personnage])
def get_personnages(token: str = Header(...)):
    if token != "secret123":
        raise HTTPException(status_code=401, detail="Token invalide")
    return personnages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tu peux mettre ["http://localhost:3000"] si besoin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
