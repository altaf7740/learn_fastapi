from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from database import Base
import uuid


class Users(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: uuid.uuid4().hex, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="user")
    
class Todos(Base):
    __tablename__ = "todos"
    
    id = Column(String, primary_key=True, default=lambda: uuid.uuid4().hex, index=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)
    priority = Column(Integer)
    owner_id = Column(String, ForeignKey("users.id"))

