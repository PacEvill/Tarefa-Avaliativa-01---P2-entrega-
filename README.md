# Tarefa Avaliativa 01 - P2 (CRUD FastAPI + PostgreSQL)

> Projeto desenvolvido para a disciplina de Laboratório de Programação Back-end.
>
> CRUD completo de tarefas utilizando FastAPI, SQLAlchemy, Alembic e PostgreSQL.

## Estrutura do Projeto
- `main.py`: Rotas da API (CRUD de tarefas)
- `models.py`: Modelos ORM (tabela tarefas)
- `schemas.py`: Schemas Pydantic (validação de dados)
- `database.py`: Conexão e sessão com o banco
- `alembic/`: Migrations do banco de dados
- `docker-compose.yml`: Sobe o PostgreSQL via Docker
- `.env`: Configuração da string de conexão
- `requirements.txt`: Dependências do projeto

## Como rodar o projeto

1. **Clone o repositório:**
	```sh
	git clone https://github.com/PacEvill/Tarefa-Avaliativa-01---P2-entrega-
	cd Tarefa-Avaliativa-01---P2-entrega-
	```
2. **Crie e ative o ambiente virtual:**
	```sh
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	```
3. **Suba o banco de dados:**
	```sh
	docker compose up -d
	```
4. **Execute as migrações Alembic:**
	```sh
	alembic upgrade head
	```
5. **Inicie a API:**
	```sh
	uvicorn main:app --reload
	```
6. **Acesse a documentação:**
	- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Funcionalidades
- Criar, listar, atualizar e deletar tarefas
- Banco de dados PostgreSQL
- Migrations com Alembic
- Documentação automática com Swagger

---

> Projeto para fins avaliativos. Qualquer dúvida, consulte o código ou abra uma issue no repositório.