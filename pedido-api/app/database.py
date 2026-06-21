from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

database = client["pedidos_db"]

pedidos_collection = database["pedidos"]