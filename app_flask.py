from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'
DB_PATH = 'biblioteca.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.close()
    return render_template('index.html', livros=livros)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form.get('titulo', '').strip()
    autor = request.form.get('autor', '').strip()
    ano = request.form.get('ano_publicizacao', '').strip()
    disponivel = 1 if request.form.get('disponivel') == 'on' else 0

    if not titulo or not autor:
        flash('Título e autor são obrigatórios!', 'danger')
        return redirect(url_for('index'))

    try:
        ano_int = int(ano) if ano else None
    except ValueError:
        flash('Ano inválido.', 'danger')
        return redirect(url_for('index'))

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO livros (titulo, autor, ano_publicacao, disponivel) VALUES (?, ?, ?, ?)',
        (titulo, autor, ano_int, disponivel)
    )
    conn.commit()
    conn.close()

    flash('Livro adicionado com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM livros WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Livro excluído.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
