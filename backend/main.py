from fastapi import FastAPI
from app.schemas import Idea
from app.models import Ideas

app = FastAPI()
ideas = Ideas()


@app.get("/idea")
async def get_idea(offset: int = 0, limit: int = 10) -> list[Idea]:
    return ideas.get(offset, limit)


@app.post("/idea")
async def post_idea(idea: Idea) -> None:
    ideas.append(idea)


@app.get("/idea/random")
async def random_idea() -> Idea | None:
    idea = ideas.random()
    return idea
