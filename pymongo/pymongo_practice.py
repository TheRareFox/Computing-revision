from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)

# Create new db
db = client["new_db"]

# Delete db
client['new_db'].command("dropDatabase")

print("\n\nInitialize empty db and collection")
print("db names:", client.list_database_names()) # will only print if db contains cols that contains data; won't print

# Create new collection
col = db['new_col']

# Delete collection
col.drop()

print("collection names:", db.list_collection_names()) # will only print if cols contains data; won't print

print("\n\ninserting docuemnt into collection...")
col.insert_one({"age":18, "name":"XXX", "social security number":1234567890})

print("db names:", db.list_collection_names()) # will only print if cols contains data; will print

print("collection names:", client.list_database_names()) # will only print if db contains cols that contains data; will print

print("document in col: ", col.find_one())


print("\n\ninserting multiple docuemnts into collection...")
col.insert_many([{"age":20, "name":"KKK", "social security number":987654321},
                 {"age":22, "name":"GGG", "social security number":9999999967}])

print("db names:", db.list_collection_names()) # will only print if cols contains data; will print

print("collection names:", client.list_database_names()) # will only print if db contains cols that contains data; will print
docs = col.find({})
docs = [doc for doc in docs]
print("Found {} documents in col: ".format(len(docs)))
for doc in docs:
    print(doc)

print("\n\nSearching for document: age=20")
docs = col.find({"age":{"$eq":20}})
docs = [doc for doc in docs] # convert from cursor to list
print("Found {} document(s) in col with age=20:".format(len(docs)))
for doc in docs:
    print(doc)



print("\n\ndropping collection...")
db["new_col"].drop()

print("db names:", db.list_collection_names()) # will only print if cols contains data; will print

print("collection names: ", client.list_database_names()) # will only print if db contains cols that contains data; will print




