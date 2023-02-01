#step1: install and import pymongo
import pymongo
import certifi
import data.mongo_setup as mongo_setup

#step2: Create a connection using MongoClient.
CONNECTION_STRING = "mongodb+srv://testuser:testpw@cluster0.gv9cbee.mongodb.net/?retryWrites=true&w=majority"
try:
  client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
except Exception:
  print("error:"+Exception)

#step3 create a db
myDb = client["Friendymap_db"]

#step4 create a collection
myCollection = myDb ["user"]

#step5 create a doc
myDoc = {
  "name":"JW",
  "password":"1234"
}

#step6 insert the doc
res = myCollection.insert_one(myDoc)

print(res.inserted_id)
print(client.list_database_names())

def main():
    moongo_setup.global_init()