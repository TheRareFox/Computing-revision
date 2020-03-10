from pymongo import MongoClient

# --- create a client to communicate to the mongo db server ---
client = MongoClient('localhost', 27017)



# --- clear/delete database ---
names = client.list_database_names()
print(names)
for name in names:
    try:
        client.drop_database(name)
    except:
        pass

print(client.list_database_names())



# --- get database ---
db = client.test_database # also works if database does not exist; will create

db = client['test_database'] # use this if database contains '-'

print(client.list_database_names())



# --- clear/delete collection from database ---
db.test_collection.drop()
db.posts.drop()



# --- get collection from db ---
# will initialize but will not display if list_collection_names()
collection = db.test_collection 
collection = db['test_collection']

print("Before insertion")
print("In db 'test_database':", db.list_collection_names()) # will return empty array; collection is empty



# --- create a post; json object aka a dictionary and insert the post ---

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"]}

collection.insert_one(post)
print("After insertion")
print("In db 'test_database':", db.list_collection_names())
