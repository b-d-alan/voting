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


def voter_verification(connection_to_votesdb, voter_ID):
    try:
        cursor = connection_to_votesdb.execute(
            """SELECT * FROM voters WHERE admission_no=?""",
            (voter_ID,),
        )
        voter = cursor.fetchone()
        if voter is None:
            raise Exception("voter not found")
        elif voter[1] == 1:
            raise Exception("voter has already voted")
        else:
            connection_to_votesdb.execute(
                """UPDATE voters SET has_voted=1 WHERE admission_no=?""",
                (voter_ID,),
            )
            connection_to_votesdb.commit()
            return True, None
    except Exception as e:
        return False, e
