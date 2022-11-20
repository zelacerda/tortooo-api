from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from spell import check_spell


app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://zelacerda.github.io",
    "https://zelacerda.github.io",
    "http://tort.ooo",
    "https://tort.ooo"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{word}")
async def check(word: str):
    return {"result": check_spell(word)}
