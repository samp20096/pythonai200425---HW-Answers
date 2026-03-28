from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    description: str

auto_increment_id = 3

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "description": "Fantasy novel"},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949, "description": "Dystopian novel"},
    {"id": 3, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008, "description": "Software dev practices"}
]

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found") # error 204 - No content

@app.post("/books")
def add_book(book: Book):
    global auto_increment_id
    auto_increment_id += 1
    new_book = {
        "id": auto_increment_id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "description": book.description
    }
    books.append(new_book)
    return {"message": "Book added successfully"}, new_book

@app.put("/books/{book_id}")
def replace_book(book_id: int, book: Book):
    for index, b in enumerate(books):
        if b['id'] == book_id:
            books[index] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.patch("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for index, b in enumerate(books):
        if b['id'] == book_id:
            if book.title:
                b['title'] = book.title
            if book.author:
                b['author'] = book.author
            if book.year:
                b['year'] = book.year
            if book.description:
                b['description'] = book.description
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, b in enumerate(books):
        if b["id"] == book_id:
            deleted = books.pop(index)
            return {"message": f"Book {deleted['id']} deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
