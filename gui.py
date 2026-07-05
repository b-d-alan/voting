import customtkinter as ctk
import tkinter as tk
import index
import sqlite3

with open("metadata.txt", "r") as metadata_fileobject:
    metadata = metadata_fileobject.read()
    db_name = metadata.split(":")[1].strip()

connection_to_db = sqlite3.connect(db_name)


def cast_vote(party_name):
    try:
        cursor = connection_to_db.execute(
            """UPDATE votes SET votes= votes+1 WHERE party_name=?""", (party_name,)
        )

        if cursor.rowcount == 0:
            raise Exception("party not found")
        else:
            connection_to_db.commit()
            return True, None
    except Exception as e:
        return False, e


app = ctk.CTk()
app.title("ELECTION")
app.geometry("1600x600")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app.iconbitmap("icon.ico")

button_frame = ctk.CTkFrame(app)

button_1 = ctk.CTkButton(
    master=button_frame,
    text="Vote for party 1",
    command=lambda: cast_vote("party1"),
)

button_2 = ctk.CTkButton(
    master=button_frame,
    text="Vote for party 2",
    command=lambda: cast_vote("party2"),
)

button_3 = ctk.CTkButton(
    master=button_frame,
    text="Vote for party 3",
    command=lambda: cast_vote("party3"),
)

button_4 = ctk.CTkButton(
    master=button_frame,
    text="Vote for party 4",
    command=lambda: cast_vote("party4"),
)

button_1.grid(row=0, column=0, padx=30)
button_2.grid(row=0, column=1, padx=30)
button_3.grid(row=0, column=2, padx=30)
button_4.grid(row=0, column=3, padx=30)
button_frame.pack(fill="x", padx=20, pady=100)
"""button_1.grid(row=0, column=1, padx=10, pady=10)
button_2.grid(row=0, column=2, padx=10, pady=10)
button_3.grid(row=0, column=3, padx=10, pady=10)
button_4.grid(row=0, column=4, padx=10, pady=10)"""
app.mainloop()
