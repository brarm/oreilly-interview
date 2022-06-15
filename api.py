#!/usr/bin/env python3

from flask import Flask
import psycopg2

connection = psycopg2.connect(database="oreilly", user="oreilly", password="hunter2", host="localhost", port=5432)

cursor = connection.cursor()
# Fetch all rows from database
# cursor.execute("SELECT count(*) from works;")
# record = cursor.fetchall()
# print(len(record))
# print(record[0][0])

#print("Data from Database:- ", record)

app = Flask(__name__)

@app.route("/")
def info():
    return '''
/all_books
/subset_id <id_from> <id_to>
/subset_author <author>
/single_id <work_id>
/single_title <title>
/single_isbn <isbn>
'''

@app.route("/all_books")
def all_books():
    cursor.execute("SELECT * from works;")
    record = cursor.fetchall()
    return str(record)

@app.route("/subset_id/<int:id_from>/<int:id_to>")
def subset_id(id_from, id_to):
    cursor.execute("SELECT count(*) from works;")
    count = int(cursor.fetchall()[0][0])
    FROM_CHECK = id_from >= 0
    TO_CHECK = id_to <= count
    RANGE_CHECK = (id_to - id_from) >= 0
    if not (FROM_CHECK and TO_CHECK and RANGE_CHECK):
        return "ERROR: incorrect range specified"
    cursor.execute(f'SELECT * FROM works where work_id >= {id_from} and work_id <= {id_to};')
    record = cursor.fetchall()
    return str(record)

@app.route("/subset_author/<string:author>")
def subset_author(author):
    cursor.execute(f"select * from public.works where works.authors = '{author}';")
    record = cursor.fetchall()
    if not len(record):
        return f"No books found with author name: {author}"
    else:
        return str(record)

@app.route("/single_id/<int:work_id>")
def single_id(work_id):
    cursor.execute(f'SELECT * FROM works where works.work_id = {work_id}')
    record = cursor.fetchall()
    if not len(record):
        return f'No book found with work_id: {work_id}'
    else:
        return str(record)

@app.route("/single_title/<string:title>")
def single_title(title):
    cursor.execute(f'SELECT * FROM works where works.title = {title}')
    record = cursor.fetchall()
    if not len(record):
        return f'No book found with title: {title}'
    else:
        return str(record)


@app.route("/single_isbn/<string:isbn>")
def single_isbn(isbn):
    cursor.execute(f'SELECT * FROM works where works.isbn = {isbn}')
    record = cursor.fetchall()
    if not len(record):
        return f'No book found with isbn: {isbn}'
    else:
        return str(record)

