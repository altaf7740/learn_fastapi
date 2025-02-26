from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Book:
    def __init__(self, id: int, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author
        
class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    

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








