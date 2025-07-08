import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from model import UFUMenu

def scrape_ufu(db: Session):
    resposta = requests.get('https://ufu.br/')
    if resposta.status_code != 200:
        return []

    soup = BeautifulSoup(resposta.content, 'html.parser')
    barra_esquerda = soup.find('ul', class_='sidebar-nav nav-level-0')
    linhas_barra = barra_esquerda.find_all('li', class_='nav-item')

    iniciar = False
    dados = []

    for li in linhas_barra:
        if 'Graduação' in li.text.strip():
            iniciar = True
        if iniciar and li.a:
            titulo = li.text.strip()
            link = "https://ufu.br" + li.a.get('href')
            # Verifica se já existe
            existente = db.query(UFUMenu).filter_by(link=link).first()
            if not existente:
                item = UFUMenu(titulo=titulo, link=link)
                db.add(item)
                dados.append({"titulo": titulo, "link": link})

    db.commit()
    return dados
