from pydantic import BaseModel


class Idea(BaseModel):
    name: str
    description: str
