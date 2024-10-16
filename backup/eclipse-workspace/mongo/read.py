from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['mydb']
print("Database created")
collection = database['product']

print(collection.find_one())
cursor = collection.find({"name":"google"})
for each in cursor:
    print(each)