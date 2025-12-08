# imports de requisitos
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
import sqlite3

# caminho da db
DB_PATH = 'biblioteca.db'

# titulo api
app = FastAPI(title="API Biblioteca")

# variaveis/formulario dos livros
class LivroIn(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: Optional[int] = None
    disponivel: bool = True

class LivroOut(LivroIn):
    id: int

# connecção com o DB a partir do caminho da DB
def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# conecta ao db executa select para listar todos os livros
@app.get("/livros", response_model=List[LivroOut])
def listar():
    conn = connect()
    query = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()

    return [
        {
            "id": row["id"],
            "titulo": row["titulo"],
            "autor": row["autor"],
            "ano_publicacao": row["ano_publicacao"],
            "disponivel": bool(row["disponivel"])
        }
        for row in query
    ]

# conecta ao db, executa select apenas de um ID específico e depois desconecta
@app.get("/livros/{id}", response_model=LivroOut)
def obter(id: int):
    conn = connect()
    row = conn.execute("SELECT * FROM livros WHERE id = ?", (id,)).fetchone()
    conn.close()

    if not row:
        raise HTTPException(404, "Livro não encontrado")

    return {
        "id": row["id"],
        "titulo": row["titulo"],
        "autor": row["autor"],
        "ano_publicacao": row["ano_publicacao"],
        "disponivel": bool(row["disponivel"])
    }

# connecta ao db, insere um livro novo, commit e depois desconecta 
@app.post("/livros", status_code=201, response_model=LivroOut)
def criar(livro: LivroIn):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO livros (titulo, autor, ano_publicacao, disponivel) VALUES (?, ?, ?, ?)",
        (livro.titulo, livro.autor, livro.ano_publicacao, 1 if livro.disponivel else 0)
    )
    conn.commit()
    novo_id = cur.lastrowid
    conn.close()

    return {**livro.dict(), "id": novo_id}

# conecta ao db e edita um livro pelo id, commit e depois desconecta

@app.put("/livros/{id}", response_model=LivroOut)
def atualizar(id: int, livro: LivroIn):
    conn = connect()
    cur = conn.cursor()

    existe = cur.execute("SELECT * FROM livros WHERE id = ?", (id,)).fetchone()
    if not existe:
        conn.close()
        raise HTTPException(404, "Livro não encontrado")

    cur.execute(
        "UPDATE livros SET titulo=?, autor=?, ano_publicacao=?, disponivel=? WHERE id=?",
        (livro.titulo, livro.autor, livro.ano_publicacao, 1 if livro.disponivel else 0, id)
    )
    conn.commit()
    conn.close()

    return {**livro.dict(), "id": id}

# conecta ao db, exclui um livro pelo id, commit e depois desconecta
@app.delete("/livros/{id}")
def deletar(id: int):
    conn = connect()
    cur = conn.cursor()

    existe = cur.execute("SELECT id FROM livros WHERE id = ?", (id,)).fetchone()
    if not existe:
        conn.close()
        raise HTTPException(404, "Livro não encontrado")

    cur.execute("DELETE FROM livros WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return {"mensagem": "Livro removido com sucesso"}