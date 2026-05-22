"""
This is the main file for the voting system.
It handles the user interface and calls the necessary functions from the index.py file to perform the required operations.
"""

from index import *
import sqlite3

with open("metadata.txt", "r") as metadata_fileobject:
    metadata = metadata_fileobject.read()
    database_name = metadata.split(":")[1].strip()


while True:
    try:
        connection_to_votesdb = sqlite3.connect(database_name)
        voter_ID = input("enter your admission number: ").strip().upper()
        success, error = voter_verification(connection_to_votesdb, voter_ID)
        if success:
            party_name = input("enter the party name you want to vote for: ")
            success, error = cast_vote(connection_to_votesdb, party_name)
            if success:
                print("vote casted successfully")
            else:
                print("error:", error)
                continue
        else:
            print("error:", error)
            continue
        connection_to_votesdb.commit()
    except Exception as e:
        print("error:", e)
        connection_to_votesdb.rollback()
    finally:
        connection_to_votesdb.close()
