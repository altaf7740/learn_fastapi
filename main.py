from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()

class Book:
    def __init__(self, id: int, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author
        
class BookSchema(BaseModel):
    id: int = Field(ge=0, description="The ID of the book")
    title: str = Field(min_length=3, description="The title of the book",)
    author: str = Field(min_length=3, description="The author of the book")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1, 
                "title": "The Great Gatsby", 
                "author": "F. Scott Fitzgerald"
            }
        }
    }
    

books = [
    Book(1, "The Great Gatsby", "F. Scott Fitzgerald"),
    Book(2, "To Kill a Mockingbird", "Harper Lee"),
    Book(3, "1984", "George Orwell"),
]


@app.get("/books")
def get_books():
    return books

@app.post("/books")
def create_book(book_schema: BookSchema):
    book = Book(**book_schema.model_dump())
    books.append(book)
    return book








