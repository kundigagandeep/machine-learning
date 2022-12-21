from fastapi import FastAPI

app = FastAPI()

BOOKS  ={
    'book_1':{'title':'Title One','author':'Author One'},
    'book_2':{'title':'Title Two','author':'Author Two'},
    'book_3':{'title':'Title Three','author':'Author Three'},
    'book_4':{'title':'Title Four','author':'Author Four'},
    'book_5':{'title':'Title Five','author':'Author Five'}
}
from enum import Enum
class BookCategory(str, Enum):
    horror = "Horror"
    self_help = "Self-Help"
    psychology = "Psychology"
    engineering = "Engineering"


@app.get("/")
def books_api():
    return BOOKS

@app.get("/books/my_books")
def read_favourite_book(book_title:str):
    return {"book_name":book_title}

@app.get("/books/{book_id}")
def read_book(book_id:int):
    return {"book_id":book_id}

@app.get("/books_category/{BookCategory}")
def read_book_cat(book_cat:BookCategory):
    if book_cat==BookCategory.horror:
        return {"book_cat":'Horror'}
    elif book_cat==BookCategory.self_help:
        return {"book_cat":'Self-Help'}
    elif book_cat==BookCategory.psychology:
        return {"book_cat":'Psychology'}
    else: 
        return {"book_cat":'Engineering'}

#Post Request
@app.post("/")
async def create_book(book_title: str, author_name:str):
    current_book_id = 0
    if len(BOOKS)>0:
        for i in BOOKS:
            new_book_id = int(i.split("_")[-1])
            if new_book_id > current_book_id:
                current_book_id = new_book_id
    BOOKS[f'book_{current_book_id+1}'] = {'title': book_title,'author':author_name}
    return {f"New Book added with id:{current_book_id+1}"}

#Update Request
@app.put('/book_name')
async def update_book_information(book_name:str, book_title:str, author_name:str):
    book_information = {'title':book_title, 'author':author_name}
    BOOKS[book_name] = book_information
    return book_information
    
