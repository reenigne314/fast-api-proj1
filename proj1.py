from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/")
async def read_books_by_category(category: str):
    book1 = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            book1.append(book)
    if book1:
        return book1
    else:
        return {"message": "No books found in this category"}
    
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.get("/books/{author}")
async def read_books_by_author(author: str):
    author1 = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            author1.append(book)
    if author1:
        return author1
    else:
        return {"message": "No books found by this author"}


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for index, book in enumerate(BOOKS):
        if book.get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[index] = updated_book
            return {"message": "Book updated successfully"}

@app.delete("/books/delete_book/{title}")
async def delete_book(title: str):
    for index in range(len(BOOKS)):
        if BOOKS[index].get('title').casefold() == title.casefold():
            BOOKS.pop(index)
            return {"message": "Book deleted successfully"}