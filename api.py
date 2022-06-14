#!/usr/bin/env python3

from flask import Flask
import psycopg2

connection = psycopg2.connect(database="oreilly", user="oreilly", password="hunter2", host="localhost", port=5432)

cursor = connection.cursor()
cursor.execute("SELECT * from works;")
# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)

app = Flask(__name__)

@app.route("/all_books")
def all_books():
    return "<p>Hello, World!</p>"

@app.route("/subset")
def subset():
    return ""

@app.route("/single")
def single():
    return ""

