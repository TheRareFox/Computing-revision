import sqlite3

#connect to db
conn = sqlite3.connect("test.db")

#cursor to do stuff for you
cur = conn.cursor()

#creates a table test1 only the first time
#creates a table:
#       test1
# id(a integer value that is unique and not empty)
# (can employ AUTOINCREMENT to increase value everytime)
# name(a text value that is not empty)   
# description(a text value)
conn.execute("CREATE TABLE IF NOT EXISTS test1(id INTEGER NOT NULL PRIMARY KEY  , 'name' text NOT NULL, 'description' text)")

#add values into table
cur.execute("INSERT INTO test1(id,name,description) values(?,?,?)",(1,"Hello","This is a test case for db testing"))

# The table now looks like
#         test1
# id      name       description
# 1      'Hello'    'This is a test case for db testing'

#commit changes
conn.commit()
#update values in table
cur.execute("UPDATE test1 SET name = 'Ben' WHERE id = ?",(1,))# NOTE: if there is only one value to be inserted, must add a comma

# The table now looks like
#         test1
# id      name       description
# 1      'Ben'    'This is a test case for db testing'

#commit changes
conn.commit()

# select values
# SELECT * - return all values
# SELECT name,id - return name and id values
cur.execute("SELECT * FROM test1")

#return the values

values = cur.fetchall()
print(values)

#returns only one value
'''
value = cur.fetchone()
print(value)
'''

# delete values
cur.execute("DELETE FROM test1 WHERE id = ?",(1,))

conn.commit()

# NOW THE TABLE IS EMPTY!!!
# NOW DO YOUR OWN EXPLORATION

#closes connection
conn.close()
