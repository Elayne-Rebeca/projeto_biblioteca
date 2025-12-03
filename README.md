# Projeto Biblioteca - Flask + FastAPI + SQLite

## Desenvolvedores
- Elayne Rebeca Machado Silva - 01726848
- Elídia Maria Silva de França  - 01702889
- Rafael Bernardo de Lima - 01688593

## Estrutura do Projeto

```
projeto_biblioteca/
├─ app_flask.py
├─ api_fast.py
├─ init_db.py        
├─ requirements.txt
├─ README.md
├─ templates/
│  └─ index.html
└─ static/
   └─ style.css
```

## Tecnologias Utilizadas

* _Python 3_
* _Flask 3.x_
* _FastAPI_
* _Uvicorn_
* _SQLite3_
* _Jinja2_
* _HTML5 / CSS_

## Executando o Projeto:

#### 1. Criação do banco de dados atravéz do script:

```bash
python init_db.py
```

#### 2. Criação do ambiente virtual:

```bash
python -m venv venv
```

#### 3. Ativar:

_Para Windows:_

```bash
venv\Scripts\activate
```
_Para macOS / Linux:_
```
source venv/bin/activate
```

#### 4. Instalar o servidor da API FastAPI
```
pip install uvicorn
```
#### 5. Instalar o framework FastAPI
```
pip install fastapi
```
#### 6. Instalar o framework Flask
```
pip install flask
```


#### 7. Iniciar a API FastAPI (porta 8000)

```bash
python -m uvicorn api_fast:app --reload --port 8000
```

*Para Acessar a documentação da API:*

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)    
    Interface (documentação interativa) para testar a API.  

- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)   
    Documentação profissional, apenas para leitura.

---

#### 8. Iniciar o servidor Flask (porta 5000)

*Obs.: Importante abrir outro terminal com o venv ativado:*

```bash
python app_flask.py
```
#### Interface Web:

* [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Endpoints da API (FastAPI)

GET(/livros) -> listar livros  
GET (/livros/{id}) -> Retornar livros  
POST (/livros) -> Cadastrar livros  
PUT (/livros/{id}) -> Atualizar livro  
DELETE (/livros/{id}) -> Remover livro  

---

## Interface Web (Flask)

O Flask fornece:

* Página inicial com listagem dos livros
* Formulário para cadastrar novos livros
* Botão para excluir livro
* Templates HTML usando Jinja2

Arquivo principal: *templates/index.html*

---
Obs.:
A API e o Flask podem rodar simultaneamente pois utilizam portas diferentes (8000 e 5000).

---