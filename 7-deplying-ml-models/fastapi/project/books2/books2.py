from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID #For unique identifier
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(title="Name of the book", min_length=1)
    author: str = Field(title="Name of the author", min_length=1)
    description: Optional[str] = Field(title="Description of the book", max_length=1000)
    rating: Optional[int] = Field(title="Rating of the book", gt=-1, lt=6) #gt(greather than) lt(less than)

BOOKS = []

@app.get('/')
async def read_all_books():
    return BOOKS

@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return BOOKS