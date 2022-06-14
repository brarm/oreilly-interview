#!/usr/bin/env python3

from flask import Flask
import psycopg2

connection = psycopg2.connect(database="oreilly", user="oreilly", password="hunter2", host="localhost", port=5432)

cursor = connection.cursor()
# Fetch all rows from database
cursor.execute("SELECT count(*) from works;")
record = cursor.fetchall()
#print(len(record))
print(record[0][0])

#print("Data from Database:- ", record)

app = Flask(__name__)

@app.route("/all_books")
def all_books():
    cursor.execute("SELECT * from works;")
    record = cursor.fetchall()
    return record

@app.route("/subset/<int:id_from>/<int:id_to>")
def subset(id_from, id_to):
    count = cursor.execute("SELECT count(*) from works;]")
    FROM_CHECK = id_from >= 0 : False
    TO_CHECK = id_to <= count : False
    RANGE_CHECK = (id_to - id_from) >=0 : False
    if not (FROM_CHECK or TO_CHECK or RANGE_CHECK):
        return "ERROR: incorrect range specified"
    cursor.execute(f'SELECT * FROM works where work_id >= {from} and work_id <= {to};')
    record = cursor.fetchall()
    return record

@app.route("/subset/<string:author>")
def subset(author):
    cursor.execute(f"select * from public.works where works.authors = '{author}';")
    record = cursor.fetchall()
    if not len(record):
        return f"No books found with author name: {author}"
    else:
        return record

@app.route("/single")
def single():
    return ""

