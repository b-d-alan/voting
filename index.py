"""
a simple program for voting
"""
import os
print(os.getcwd())
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS votes 
              ( id INTEGER PRIMARY KEY AUTOINCREMENT,
               party TEXT NOT NULL,
               votes INTEGER DEFAULT 0)""" )