from index import *
import sqlite3

with open("metadata.txt", "r") as metadata_fileobject:
    metadata = metadata_fileobject.read()
    database_name = metadata.split(":")[1].strip()

connection_to_votesdb = sqlite3.connect(database_name)

while True:
    voter_ID = input("enter your admission number: ").strip().lower()
    success, error = voter_verification(connection_to_votesdb, voter_ID)
    if success:
        party_name = input("enter the party name you want to vote for: ")
        success, error = cast_vote(connection_to_votesdb, party_name)
        if success:
            print("vote casted successfully")
        else:
            print("error:", error)
    else:
        print("error:", error)
