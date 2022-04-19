import os
from pymongo import MongoClient

mongo_atlas_pswd = os.getenv('mongo_atlas_pswd')

client = MongoClient(f"mongodb+srv://rahulm:{mongo_atlas_pswd}@cluster0.4m8va.mongodb.net/greenhouse_data?retryWrites=true&w=majority")

db = client['greenhouse_data']