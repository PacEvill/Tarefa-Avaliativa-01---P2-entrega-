from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Tarefa
from schemas import TarefaCreate, TarefaResponse

app = FastAPI()

# CREATE
@app.post("/tarefas/", response_model=TarefaResponse)
def criar_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db)):
	db_tarefa = Tarefa(**tarefa.dict())
	db.add(db_tarefa)
	db.commit()
	db.refresh(db_tarefa)
	return db_tarefa

# READ ALL
@app.get("/tarefas/", response_model=List[TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
	return db.query(Tarefa).all()

# READ ONE
@app.get("/tarefas/{tarefa_id}", response_model=TarefaResponse)
def obter_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
	tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
	if not tarefa:
		raise HTTPException(status_code=404, detail="Tarefa não encontrada")
	return tarefa

# UPDATE
@app.put("/tarefas/{tarefa_id}", response_model=TarefaResponse)
def atualizar_tarefa(tarefa_id: int, tarefa_update: TarefaCreate, db: Session = Depends(get_db)):
	tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
	if not tarefa:
		raise HTTPException(status_code=404, detail="Tarefa não encontrada")
	tarefa.titulo = tarefa_update.titulo
	tarefa.descricao = tarefa_update.descricao
	db.commit()
	db.refresh(tarefa)
	return tarefa

# DELETE
@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
	tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
	if not tarefa:
		raise HTTPException(status_code=404, detail="Tarefa não encontrada")
	db.delete(tarefa)
	db.commit()
	return {"ok": True}
