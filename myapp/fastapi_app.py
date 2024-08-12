from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    isbn: str

def create_fastapi_app_with_django_integration(books: List[Book] = []) -> FastAPI:
    app = FastAPI()

    @app.get("/books/")
    async def get_all_books():
        return books

    @app.post("/books/")
    async def add_book(book: Book):
        books.append(book)
        return book

    @app.get("/books/{isbn}/")
    async def get_book_by_isbn(isbn: str):
        for book in books:
            if book.isbn == isbn:
                return book
        raise HTTPException(status_code=404, detail="Book not found")

    @app.put("/books/{isbn}/")
    async def update_book_by_isbn(isbn: str, updated_book: Book):
        for i, book in enumerate(books):
            if book.isbn == isbn:
                books[i] = updated_book
                return updated_book
        raise HTTPException(status_code=404, detail="Book not found")

    @app.delete("/books/{isbn}/")
    async def delete_book_by_isbn(isbn: str):
        for i, book in enumerate(books):
            if book.isbn == isbn:
                del books[i]
                return {"message": "Book deleted successfully"}
        raise HTTPException(status_code=404, detail="Book not found")

    return app
