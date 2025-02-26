from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from starlette import status

from database import engine, SessionLocal
import models
import schemas

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books")
def get_books(id: UUID4 | None = None, db: Session = Depends(get_db)):
    if id:
        book = db.query(models.Book).filter(models.Book.id == id.hex).first()
        if book:
            return book
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        books = db.query(models.Book).all()
        return books

@app.post("/books", response_model=schemas.BookSchema, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookSchema, db: Session = Depends(get_db)):
    book_dict = book.model_dump()
    new_book = models.Book(**book_dict)
    db.add(new_book)
    db.commit()
    return new_book

@app.delete("/books/{id}")
def delete_book(id: UUID4, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id.hex).first()
    if book:
        db.delete(book)
        db.commit()
        return {"message": "Book deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")