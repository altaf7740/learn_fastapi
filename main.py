from fastapi import FastAPI, HTTPException

app = FastAPI()

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
]


@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/filter-by-author")
def get_books_by_author(author: str):
    return [book for book in books if book["author"] == author]

@app.post("/books")
def create_book(book: dict):
    books.append(book)
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: dict):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            books[i] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            books.pop(i)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")


