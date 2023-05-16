import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

DB_NAME = 'todo_application'
USER = os.getenv('API_USER')
PASSWORD = os.getenv('API_PASSWORD')

client = MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@cluster0.niruen4.mongodb.net/?retryWrites=true&w=majority")


db = client[DB_NAME]
collection_name = db["todos_app"]