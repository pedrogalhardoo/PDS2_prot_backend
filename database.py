# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# ✅ Carrega variáveis do arquivo .env, se ele existir (uso local)
load_dotenv()

# ✅ Pega as variáveis de ambiente (funciona tanto local quanto no CI com GitHub Secrets)
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
host = os.getenv("DB_HOST")

# 🔧 Cria a URL de conexão com base nas variáveis
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

# 🔌 SQLAlchemy engine e session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency para FastAPI ou testes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
