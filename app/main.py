from fastapi import FastAPI
from . import Idea, Ideas

app = FastAPI()
ideas = Ideas()


@app.get("/idea")
async def get_idea(offset: int = 0, limit: int = 10) -> list[Idea]:
    return ideas.get(offset, limit)


@app.post("/idea")
async def post_idea(idea: Idea):
    ideas.append(idea)
