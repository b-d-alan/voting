"""
this file is going to have just the backend logic for voting
functions like voter verification and vote casting will be implemented here
"""

import sqlite3


def cast_vote(party_name):
    with open("metadata.txt", "r") as metadata_fileobject:
        metadata = metadata_fileobject.read()
        db_name = metadata.split(":")[1].strip()
    print("cast_vote called", db_name, party_name)
    try:
        connection_to_db = sqlite3.connect(db_name)
        cursor = connection_to_db.execute(
            """UPDATE votes SET votes= votes+1 WHERE party_name=?""", (party_name,)
        )
        print("query complete", db_name, party_name)
        if cursor.rowcount == 0:
            raise Exception("party not found")
        else:
            connection_to_db.commit()
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
            return True, None
    except Exception as e:
        return False, e
