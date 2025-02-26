from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel, Field
from starlette import status
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
    Book(2, "The Great Gatsby", "kingo"),
    Book(3, "To Kill a Mockingbird", "Harper Lee"),
    Book(4, "1984", "George Orwell"),
]


@app.get("/books/{book_title}")
def get_books(book_title: str = Path(min_length=3), book_id: int = Query(gt=0)):
    for book in books:
        if book.title == book_title and book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book_schema: BookSchema):
    new_book = Book(**book_schema.model_dump())
    books.append(new_book)
    return new_book
