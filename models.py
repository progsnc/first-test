from pydantic import BaseModel


class Post(BaseModel):
    userId: int
    title: str
    body: str

