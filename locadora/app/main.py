from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from . import crud

"""
    A ideia é montar um banco de dados relacional que faça uma 'locadora virtual' via API!
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        crud.criar_tabela()
        print("Banco de dados inicializado com sucesso.")
    except Exception as e:
        print(f"Erro ao iniciar o banco: {e}")
    
    yield
    print("Servidor finalizado.")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def redirect():
    """Redireciona a raiz para a documentação automática"""
    return RedirectResponse(url="/docs")


@app.get("/filmes")
def lista_filmes():
    return crud.listar_filmes()


@app.get("/filmes/{titulo}")
def buscar(titulo: str):
    filme = crud.buscar_filmes(titulo)

    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme


@app.put("/filmes/remover/{titulo}/{quantidade}")
def remover(titulo: str, quantidade: int):
    filme = crud.remover_filmes(titulo, quantidade)
    if not filme:
        return {"erro": "Filme não encontrado ou quantidade já é zero"}
    return filme


@app.post("/filmes/incluir/{titulo}/{quantidade}")
def incluir(titulo: str, quantidade: int):

    filme_existente = crud.buscar_filmes(titulo)

    if filme_existente:
        return {"erro": f"O filme '{titulo}' já existe em nosso catálogo!"}
    filme = crud.inclui_filmes(titulo, quantidade)

    if not filme:
        return {"erro": "Não foi possível incluir o filme"}
    return filme


@app.delete("/filmes/{titulo}")
def excluir(titulo: str):

    filme_existente = crud.buscar_filmes(titulo)

    if not filme_existente:
        raise HTTPException(
            status_code=404, detail=f"O filme '{titulo}' não existe em nosso catálogo!"
        )

    filme = crud.excluir_filmes(titulo)
    return filme
