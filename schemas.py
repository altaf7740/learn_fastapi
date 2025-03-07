from pydantic import BaseModel, Field

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str

class CreateTodoRequest(BaseModel):
    title: str
    description: str
    priority: int
    completed: bool
