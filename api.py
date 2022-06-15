#!/usr/bin/env python3

from flask import Flask
from os import getenv
import psycopg2

DATABASE = getenv('DATABASE', 'oreilly')
DB_USER = getenv('DB_USER', 'oreilly')
DB_PASSWORD = getenv('DB_PASSWORD', 'hunter2')
DB_HOST = getenv('DB_HOST', 'localhost')
DB_PORT = getenv('DB_PORT', 5432)

connection = psycopg2.connect(
        database=DATABASE, 
        user=DB_USER, 
        password=DB_PASSWORD, 
        host=DB_HOST, 
        port=DB_PORT)
cursor = connection.cursor()

app = Flask(__name__)

TABLE_NAME = 'works'
ID_LABEL = 'work_id'

# default path returns API usage
@app.route('/')
def info():
    return '''
/all_books
/subset_id <id_FROM> <id_to>
/subset_author <author>
/single_id <work_id>
/single_isbn <isbn>
'''

# GET all books in database
@app.route('/all_books', methods=['GET'])
def all_books():
    cursor.execute('SELECT * FROM {TABLE_NAME}')
    record = cursor.fetchall()
    return str(record)

# GET subset of books by ids in range, inclusive
@app.route('/subset_id/<int:id_FROM>/<int:id_to>', methods=['GET'])
def subset_id(id_FROM, id_to):
    cursor.execute(f'SELECT count(*) FROM {TABLE_NAME}')
    count = int(cursor.fetchall()[0][0])
    FROM_CHECK = id_FROM >= 0
    TO_CHECK = id_to <= count
    RANGE_CHECK = (id_to - id_FROM) > 0
    if not (FROM_CHECK and TO_CHECK and RANGE_CHECK):
        return 'ERROR: incorrect range specified. Ensure id\'s within table limits and id_to > id_from'
    else:
        cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE {ID_LABEL} >= {id_FROM} and {ID_LABEL} <= {id_to}')
        record = cursor.fetchall()
        return str(record)

# GET single book by id
@app.route('/single_id/<int:book_id>', methods=['GET'])
def single_id(book_id):
    cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE {ID_LABEL} = {book_id}')
    record = cursor.fetchall()
    if not len(record):
        return f'No book found with id: {book_id}'
    else:
        return str(record)

# GET single book by isbn
@app.route('/single_isbn/<string:isbn>', methods=['GET'])
def single_isbn(isbn):
    cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE isbn = {isbn}::VARCHAR')
    record = cursor.fetchall()
    if not len(record):
        return f'No book found with ISBN: {isbn}'
    else:
        return str(record)

