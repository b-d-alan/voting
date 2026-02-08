"""
a simple program for voting
"""
import os
print(os.getcwd())
import sqlite3

conn = sqlite3.connect("test.db")