from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import Idea
from app.models import Ideas

app = FastAPI()
ideas = Ideas()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/idea")
async def get_idea(offset: int = 0, limit: int = 10) -> list[Idea]:
    return ideas.get(offset, limit)


@app.post("/idea")
async def post_idea(idea: Idea) -> None:
    ideas.append(idea)


@app.get("/idea/random")
async def random_idea() -> Idea | None:
    return ideas.random()


@app.get("/idea/count")
async def count_idea() -> int:
    return ideas.count()
