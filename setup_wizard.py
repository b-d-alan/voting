"""
setup_wizard to create database, tables and import voters list
"""

import sqlite3
import csv


def databse_setup(useless_parameter=None,database_name):
    connection_to_db = sqlite3.connect(database_name)
    connection_to_db.execute("""CREATE TABLE IF NOT EXISTS votes(
                    Id integer PRIMARY KEY AUTOINCREMENT,
                    party_name TEXT UNIQUE,
                    votes INTEGER)
                    """)
    connection_to_db.execute("""CREATE TABLE IF NOT EXISTS voters(
                    admission_no TEXT PRIMARY KEY,
                    has_voted INTEGER DEFAULT 0
                    )""")
    connection_to_db.commit()
    print("Creation successful")
    return connection_to_db



def add_party(connection_to_db, party_name):
    try:
        connection_to_db.execute(
            """INSERT INTO votes(
            party_name, votes) VALUES (?,?)""",
            (party_name, 0),
        )
        connection_to_db.commit()
        print(f"party({party_name}) added")

    except Exception as e:
        print("error", e)


def import_data(connection_to_db, csv_file_name):
    try:
        admission_number_header = input(
            "what is the header name for the admisssion number column"
        )
        admission_no_column_no = None
        with open(f"{csv_file_name}.csv", "r") as csv_file_object:
            csv_reader = csv.reader(csv_file_object)
            csv_reader_list = list(csv_reader)
            header = csv_reader_list[0]
            csv_reader_list = csv_reader_list[1:]
            for column_no in range(len(header)):
                if header[column_no] == admission_number_header:
                    admission_no_column_no = column_no
                    break
            if admission_no_column_no is None:
                raise Exception("admission number column not found")
            for row in csv_reader_list:
                connection_to_db.execute(
                    """INSERT INTO voters(admission_no) VALUES (?)""",
                    (row[admission_no_column_no],),
                )
            connection_to_db.commit()
        print("import successful")
    except Exception as e:
        print("error", e)


command_function_hashing = {
    "add_party": add_party,
    "import_data": import_data,
    "setup_database": databse_setup,
}
while True:
    command = input("enter command")
    command_keyword = command.split()[0]
    command_argument = " ".join(command.split()[1:])
    if command_keyword in command_function_hashing:
        command_function_hashing[command_keyword](databse_setup(),command_argument)
    elif command.strip().lower()=="exit":
        break
    else:
        print("invalid command")
