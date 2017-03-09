#sql.py - Creates a SQLitw3 table and populates it with data

import sqlite3 #Imports SQLite Controller

#Create a new database if the database doesn't already exists

#Creating and starting connection with our database
with sqlite3.connect("blog.db") as connection: 
    # get a cursor object used to execute SQL commands
    cursor = connection.cursor()
    
    #create our table
    cursor.execute(""" CREATE TABLE posts (title TEXT, post TEXT) """)
    
    # insert some dummy data into the table
    cursor.execute("INSERT INTO posts VALUES ('Good', 'Im good.')")
    cursor.execute("INSERT INTO posts VALUES ('Well', 'Im well.')")
    cursor.execute("INSERT INTO posts VALUES ('Excellent', 'Im excelent.')")