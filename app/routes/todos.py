from fastapi import APIRouter, HTTPException
from models import Todo
from database import read_todos, write_todos

router = APIRouter()

@router.get("/", summary="Listar todos os to-dos", tags=["To-Dos"])
async def get_todos():
    """Retorna todos os to-dos."""
    return read_todos()


@router.post("/", summary="Criar um novo to-do", tags=["To-Dos"])
async def create_todo(todo: Todo):
    """Cria um novo to-do."""
    todos = read_todos()
    todo.id = len(todos) + 1
    todos.append(todo.dict())
    
    write_todos(todos)
    
    return todo


@router.put("/{todo_id}", summary="Atualizar um to-do", tags=["To-Dos"])
async def update_todo(todo_id: int, todo: Todo):
    """Atualiza um to-do existente."""
    todos = read_todos()
    
    for index, t in enumerate(todos):
        if t["id"] == todo_id:
            todos[index] = todo.dict()
            todos[index]["id"] = todo_id
            
            write_todos(todos)
            
            return todos[index]
    raise HTTPException(status_code=404, detail="To-Do não encontrado")


@router.delete("/{todo_id}", summary="Excluir um to-do", tags=["To-Dos"])
async def delete_todo(todo_id: int):
    """Exclui um to-do pelo ID."""
    todos = read_todos()
    todos = [t for t in todos if t["id"] != todo_id]
    
    write_todos(todos)
    
    return {"message": "To-Do excluído com sucesso"}
