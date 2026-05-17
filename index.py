"""
this file is going to have just the backend logic for voting
"""


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
