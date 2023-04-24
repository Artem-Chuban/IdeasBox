from pymongo import MongoClient
from ..schemas import Idea


class Ideas:
    def __init__(self):
        self.__client = MongoClient(host="mongodb://mongodb:27017")
        self.__db = self.__client.get_database("IdeasBox")
        self.__collection = self.__db.get_collection("ideas")

    def append(self, idea: Idea) -> None:
        self.__collection.insert_one({"name": idea.name, "description": idea.description})

    def get(self, offset: int, limit: int) -> list[Idea]:
        cursor = self.__collection.find().skip(offset).limit(limit)
        return [Idea(name=document["name"], description=document["description"]) for document in cursor]

    def random(self) -> Idea | None:
        if self.__collection.count_documents({}) == 0:
            return None
        return self.__collection.aggregate([{"$sample": {"size": 1}}]).next()
