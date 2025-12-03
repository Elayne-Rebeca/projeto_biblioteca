# import
import sqlite3

# definição de inicialização do db, ciração da table e retorno se foi criado.
def init_db():
    conn = sqlite3.connect('biblioteca.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano_publicacao INTEGER,
        disponivel INTEGER NOT NULL DEFAULT 1
    );
    ''')
    conn.commit()
    conn.close()
    print("Banco biblioteca.db criado/atualizado com tabela livros.")

if __name__ == '__main__':
    init_db()
