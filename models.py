from sqlalchemy import Column, String, DateTime
from database import Base
import uuid
from datetime import datetime

class Book(Base):
    __tablename__ = "books"
    
    id = Column(String, primary_key=True, default=lambda: uuid.uuid4().hex, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.now)

    