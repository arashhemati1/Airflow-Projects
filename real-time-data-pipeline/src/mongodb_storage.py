from pymongo import MongoClient

def store_in_mongodb():
    client = MongoClient('localhost', 27017)
    db = client.my_database
    collection = db.my_collection
    collection.insert_one({'message': 'Hello from MongoDB'})
    print("Data stored in MongoDB")
