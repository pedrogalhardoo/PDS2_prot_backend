from fastapi import FastAPI, status, Depends
from typing import List
# from fastapi.params import Body
# from pydantic import BaseModel
import classes
import model
from database import engine, get_db
from sqlalchemy.orm import Session
from scraping import scrape_ufu
from model import UFUMenu
from fastapi.middleware.cors import CORSMiddleware

def init_db():
    model.Base.metadata.create_all(bind=engine)

init_db()

app = FastAPI()

origins = [
    "http://localhost:3000",  # React padrão
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class Mensagem(BaseModel):
#     titulo: str
#     conteudo: str
#     publicada: bool = True

@app.get("/")
def read_root():
    return {"Hello": "lala"}

# @app.post("/criar")
# def criar_valores(res: dict = Body(...)):
#     print(res)
#     return {"Mensagem": f"lala: {res['lala']} lele: {res['lele']}"}

# @app.post ("/criar")
# def criar_valores(nova_mensagem: classes.Mensagem):
#     print(nova_mensagem)
#     return {"Mensagem": f"Titulo: {nova_mensagem.titulo} Conteudo: {nova_mensagem.conteudo} Publicada: {nova_mensagem.publicada}"}

@app.post("/criar", status_code=status.HTTP_201_CREATED)
def criar_valores (nova_mensagem: classes.Mensagem, db: Session = Depends (get_db)):
    mensagem_criada = model.Model_Mensagem(**nova_mensagem.model_dump())
    db.add(mensagem_criada)
    db.commit()
    db.refresh(mensagem_criada)
    return {"Mensagem": mensagem_criada}

@app.get("/quadrado/{num}")
def square(num: int):
    return num ** 2

@app.post("/scrape", status_code=201)
def executar_scraping(db: Session = Depends(get_db)):
    dados_inseridos = scrape_ufu(db)
    return {"dados_salvos": dados_inseridos}

@app.get("/mensagens", response_model=List[classes.Mensagem], status_code=status.HTTP_200_OK)
async def buscar_valores(db: Session = Depends (get_db), skip: int = 0, limit: int=100):
    mensagens = db.query(model.Model_Mensagem).offset(skip).limit(limit).all()
    return mensagens