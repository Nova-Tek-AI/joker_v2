# all the books routes are going to go here
from fastapi import APIRouter

from src.schemas.book import CreateBook


# example of a class in Python
class Cat():
    name:str
    length: float
    weight: float

    def __init__(self, name: str, length: str, weight: str):
        self.name = name
        self.length = length
        self.weight = weight

# we create an entity of Cat class called eve
eve = Cat(name="eve", length=12.3, weight=2.3)

# we are creating an entity of APIRouter called router. With an initialization parameter called books
router = APIRouter(tags=["books"])

books = []

@router.post("/hello-books")
async def hello_books():
    return "Hello Books!"


@router.get("/")
async def get_books():
    return books


@router.post("/")
async def create_book(create_book: CreateBook):
    books.append(create_book.model_dump())
    return books
