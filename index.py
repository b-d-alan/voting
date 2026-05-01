"""
a simple program for voting
this file is going to have just the backend logic
"""

import os
import sqlite3

"""print(os.getcwd())

connection_object_to_testdb = sqlite3.connect("test.db")
# ":memory:" for an inmemory database
cursor = connection_object_to_testdb.cursor()
# cursor.execute(\"""CREATE TABLE test_table(
#               party text,
#               candidate text,
#               votes integer)\""")

# cursor.execute("INSERT INTO test_table VALUES ('party_2','candidate_2',0)")

# connection_object_to_testdb.commit()

# cursor.fetchone()

# cursor.fetchmany(number)

cursor.execute("SELECT * FROM test_table  ")
print([entry for entry in cursor.fetchall()])
print(cursor.fetchall(), type(cursor.fetchall()), sep="\n")


connection_object_to_testdb.commit

connection_object_to_testdb.close()"""

connection_to_votesdb = sqlite3.connect("votes.db")
connection_to_votesdb.execute("""CREATE TABLE IF NOT EXISTS votes(
               Id integer PRIMARY KEY AUTOINCREMENT,
               party_name TEXT UNIQUE,
               votes INTEGER)""")
connection_to_votesdb.commit()


def add_party(connection_to_votesdb, party_name):
    try:
        connection_to_votesdb.execute(
            """INSERT INTO votes(
            party_name, votes) VALUES (?,?)""",
            (party_name, 0),
        )
        connection_to_votesdb.commit()
        return True, None

    except Exception as e:
        return False, e


def cast_vote(connection_to_votesdb, party_name):
    try:
        cursor = connection_to_votesdb.execute(
            """UPDATE votes SET votes= votes+1 WHERE party_name=?""",
            (party_name,),
        )
        connection_to_votesdb.commit()
        if cursor.rowcount == 0:
            raise Exception("party not found")
        else:
            return True, None
    except Exception as e:
        return False, e
