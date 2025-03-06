from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todos
import schemas
from .auth import get_current_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(user: dict = Depends(get_current_user), db: Session = Depends(get_db), todo_request: schemas.CreateTodoRequest = Body(...)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get("id"))
    db.add(todo_model)
    db.commit()
    return todo_model

@router.get("/user", status_code=status.HTTP_200_OK)
async def list_todos_by_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    todos_models = db.query(Todos).filter(Todos.owner_id == user.get("id")).all()
    return todos_models

@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo(todo_id: str, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")
    