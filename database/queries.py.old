import sqlite3

conn = sqlite3.connect("database/people.sqlite")

cur = conn.cursor()

cur.execute("SELECT *  FROM person")

people = cur.fetchall()
for person in people:
    print(person)