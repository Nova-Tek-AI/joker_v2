from pydantic import BaseModel


class CreateBook(BaseModel):
    name: str
    author: str
