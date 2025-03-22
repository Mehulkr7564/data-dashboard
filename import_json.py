import json
from pymongo import MongoClient

# MongoDB se connect karna
client = MongoClient("mongodb://localhost:27017/")
db = client["dashboardDB"]
collection = db["insights"]

# JSON file read karke database me insert karna
with open("jsondata.json", encoding="utf-8") as f:
    data = json.load(f)
    collection.insert_many(data)

print("✅ Data Imported Successfully!")
