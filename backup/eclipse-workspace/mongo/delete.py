from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['mydb']
collection = database['product']
collection.delete_one({"name":"iphone"})

cursor = collection.find({"name":"iphone"})
for each in cursor:
    print(each)