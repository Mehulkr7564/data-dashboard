from pymongo import MongoClient

# MongoDB se connect karo
client = MongoClient("mongodb://localhost:27017/")
db = client["dashboardDB"]
collection = db["insights"]
