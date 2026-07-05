import customtkinter as ctk
import tkinter as tk
import index
from PIL import Image

with open("metadata.txt", "r") as metadata_fileobject:
    metadata = metadata_fileobject.read()
    db_name = metadata.split(":")[1].strip()


window = ctk.CTk()
window.title("ELECTION")
window.geometry("1600x600")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
window.iconbitmap("icon.ico")

party_img = ctk.CTkImage(
    light_image=Image.open(r"party_logo.png"),
    dark_image=Image.open(r"party_logo.png"),
    size=(100, 100),
)

button_frame = ctk.CTkFrame(window)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

party_img_label1 = ctk.CTkLabel(button_frame, text="", image=party_img)
party_img_label2 = ctk.CTkLabel(button_frame, text="", image=party_img)
party_img_label3 = ctk.CTkLabel(button_frame, text="", image=party_img)
party_img_label4 = ctk.CTkLabel(button_frame, text="", image=party_img)


button_1 = ctk.CTkButton(
    master=button_frame,
    text="Vote for party 1",
    font=("Arial", 20, "bold"),
    height=40,
    corner_radius=20,
    command=lambda: index.cast_vote(db_name, "party1"),
)

button_2 = ctk.CTkButton(
    master=button_frame,
    text="Vote for party 2",
    font=("Arial", 20, "bold"),
    height=40,
    corner_radius=20,
    command=lambda: index.cast_vote(db_name, "party2"),
)

button_3 = ctk.CTkButton(
    master=button_frame,
    text="Vote for party 3",
    font=("Arial", 20, "bold"),
    height=40,
    corner_radius=20,
    command=lambda: index.cast_vote(db_name, "party3"),
)

button_4 = ctk.CTkButton(
    master=button_frame,
    text="Vote for party 4",
    font=("Arial", 20, "bold"),
    height=40,
    corner_radius=20,
    command=lambda: index.cast_vote(db_name, "party4"),
)

button_1.grid(row=1, column=0, padx=50, sticky="ew")
button_2.grid(row=1, column=1, padx=50, sticky="ew")
button_3.grid(row=1, column=2, padx=50, sticky="ew")
button_4.grid(row=1, column=3, padx=50, sticky="ew")
party_img_label1.grid(row=0, column=0, pady=20)
party_img_label2.grid(row=0, column=1, pady=20)
party_img_label3.grid(row=0, column=2, pady=20)
party_img_label4.grid(row=0, column=3, pady=20)
button_frame.pack(fill="x", padx=20, pady=100)
window.mainloop()
