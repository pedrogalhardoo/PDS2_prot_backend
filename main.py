from fastapi import FastAPI, status, Depends
# from fastapi.params import Body
# from pydantic import BaseModel
import classes
import model
from database import engine, get_db
from sqlalchemy.orm import Session

def init_db():
    model.Base.metadata.create_all(bind=engine)

# e só execute isso manualmente, por exemplo:
if __name__ == "__main__":
    init_db()

app = FastAPI()

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

