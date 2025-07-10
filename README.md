# 🧠 Backend - Mensagens App UFU

Este é o backend do projeto **Mensagens App**, desenvolvido com **FastAPI**, **SQLAlchemy** e **PostgreSQL**, com integração via **scraping** do site da UFU.

---

## 🚀 Tecnologias

- [x] Python 3.13+
- [x] FastAPI
- [x] SQLAlchemy
- [x] PostgreSQL
- [x] Uvicorn
- [x] Requests + BeautifulSoup
- [x] dotenv

---

# 📬 Mensagens APP - Full Stack UFU

Projeto Full Stack desenvolvido para prática de integração entre **FastAPI** e **React**, com persistência de dados em **PostgreSQL** e extração de links via scraping no site da [UFU](https://ufu.br).

---


## ⚙️ Tecnologias Utilizadas

### Backend (API)
- FastAPI
- SQLAlchemy
- PostgreSQL
- BeautifulSoup (scraping)
- Uvicorn (ASGI server)

### Frontend
- React.js
- Bootstrap 5
- Axios

---

## 🚀 Como Executar o Projeto

### 🔧 Requisitos
- Python 3.11+ e `pip`
- Node.js e `npm`
- PostgreSQL
- Git

---

### 🐍 Backend

```bash
# 1. Acesse a pasta do backend
cd backend

# 2. Ative o ambiente virtual (venv)
.\venv\Scripts\activate      # Windows
# source venv/bin/activate   # Linux/Mac

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação FastAPI
uvicorn main:app --reload
A API estará disponível em: http://localhost:8000

💻 Frontend
bash
Copiar
Editar
# 1. Acesse a pasta do frontend
cd front_end

# 2. Instale os pacotes
npm install

# 3. Execute a aplicação React
npm start