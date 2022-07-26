import pymongo
client = pymongo.MongoClient("mongodb+srv://arunkurhade:Shreeganesh21@arunkurhade.kapad.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" :"Arun",
    "email" :"arun.kurhade2121@gmail.com",
    "surname" :"kurhade"
}
db1 = client['MongoDBTest']
coll = db1['test']
coll.insert_one(d)
