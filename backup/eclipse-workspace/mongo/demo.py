from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['mydb']
print("Database created")
collection = database['product']
print("collection created")

products = [{
    "name":"Iphone",
    "price":1200
    },
    {
    "name":"samsung",
    "price":400
    },
    {
    "name":"google",
    "price":500
    }]
result = collection.insert_many(products)
print(result.inserted_ids)