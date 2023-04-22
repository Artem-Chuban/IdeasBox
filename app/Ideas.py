from pymongo import MongoClient
from . import Idea


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
