"""
Create a FastAPI application with Django integration.

This module provides a FastAPI application integrated with Django.
It includes CRUD operations for books, identified by their ISBN.
"""

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Book(BaseModel):
    """Represents a book with a title, author, and ISBN."""

    title: str
    author: str
    isbn: str


def create_fastapi_app(books: List[Book] = None) -> FastAPI:
    """
    Create a FastAPI application with Django integration.

    Args:
        books (List[Book]): A list of Book objects, defaults to an empty list.

    Returns:
        FastAPI: The FastAPI application instance.
    """
    if books is None:
        books = []

    app = FastAPI()

    @app.get("/books/")
    async def get_all_books():
        """Retrieve all books."""
        return books

    @app.post("/books/")
    async def add_book(book: Book):
        """
        Add a new book to the collection.

        Args:
            book (Book): The book to be added.

        Returns:
            Book: The added book.
        """
        books.append(book)
        return book

    @app.get("/books/{isbn}/")
    async def get_book_by_isbn(isbn: str):
        """
        Retrieve a book by its ISBN.

        Args:
            isbn (str): The ISBN of the book.

        Returns:
            Book: The book with the given ISBN.

        Raises:
            HTTPException: If the book is not found.
        """
        for book in books:
            if book.isbn == isbn:
                return book
        raise HTTPException(status_code=404, detail="Book not found")

    @app.put("/books/{isbn}/")
    async def update_book_by_isbn(isbn: str, updated_book: Book):
        """
        Update an existing book by its ISBN.

        Args:
            isbn (str): The ISBN of the book to update.
            updated_book (Book): The updated book data.

        Returns:
            Book: The updated book.

        Raises:
            HTTPException: If the book is not found.
        """
        for i, book in enumerate(books):
            if book.isbn == isbn:
                books[i] = updated_book
                return updated_book
        raise HTTPException(status_code=404, detail="Book not found")

    @app.delete("/books/{isbn}/")
    async def delete_book_by_isbn(isbn: str):
        """
        Delete a book by its ISBN.

        Args:
            isbn (str): The ISBN of the book to delete.

        Returns:
            dict: A message confirming the deletion.

        Raises:
            HTTPException: If the book is not found.
        """
        for i, book in enumerate(books):
            if book.isbn == isbn:
                del books[i]
                return {"message": "Book deleted successfully"}
        raise HTTPException(status_code=404, detail="Book not found")

    return app
