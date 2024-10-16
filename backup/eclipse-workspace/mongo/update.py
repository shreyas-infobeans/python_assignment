from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['mydb']
collection = database['product']
print("Database created")
filter = {"name":"samsung"}

collection.update_one(filter,{"$set":{"price":3}})

cursor = collection.find({"name":"samsung"})
for each in cursor:
    print(each)