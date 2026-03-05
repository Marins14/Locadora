from fastapi import FastAPI
from . import crud

"""
    A ideia é montar um banco de dados relacional que faça uma 'locadora virtual' via API!
"""


app = FastAPI()

@app.get("/filmes")
def lista_filmes():
    return crud.listar_filmes()

@app.get("/filmes/{titulo}")
def buscar(titulo:str):
    return crud.buscar_filmes(titulo)

@app.put("/filmes/{titulo}/remover")
def remover(titulo: str):
    filme = crud.remover_filmes(titulo)
    if not filme:
        return {"erro": "Filme não encontrado ou quantidade já é zero"}
    return filme

@app.put("/filmes/incluir/{titulo}/{quantidade}")
def incluir(titulo: str, quantidade: int):
    filme = crud.inclui_filmes(titulo, quantidade)

    if not filme:
        return {"Erro": "Não foi possível seguir com a inclusão do filme"}

    return filme