from fastapi import FastAPI
from pydantic import BaseModel


class Idea(BaseModel):
    name: str
    description: str


class Ideas:
    def __init__(self):
        self.__ideas: list[Idea] = []

    def append(self, idea: Idea) -> None:
        self.__ideas.append(idea)

    def get(self, offset: int, count: int) -> list[Idea]:
        return self.__ideas[offset:offset + count]


app = FastAPI()
ideas = Ideas()


@app.get("/idea")
async def get_idea(offset: int = 0, count: int = 10) -> list[Idea]:
    return ideas.get(offset, count)


@app.post("/idea")
async def post_idea(idea: Idea):
    ideas.append(idea)
