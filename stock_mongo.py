import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL')
DATABASE_NAME = 'neil'
COLLECTION_NAME = 'stock'

def init_mongo():
    client = MongoClient(MONGODB_URL)
    db = client[DATABASE_NAME]
    return db

def add_stock(name, price, operator="less_than"):
        db = init_mongo()
        db.stocks.insert_one({
            "name": name,
            "price": price,
            "operator": operator
        })

def remove_stock(name):
    db = init_mongo()
    db.stocks.delete_one({
        "name": name
    })

def get_stocks():
    db = init_mongo()
    cursor = db.stocks.find()
    return list(cursor)

# add_stock("2330", 705, 'less_then')
# add_stock("2330", 705, 'greater_then')
# remove_stock("2330")
print(get_stocks())