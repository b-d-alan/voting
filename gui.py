import customtkinter as ctk
import index

app = ctk.CTk()
app.title("ELECTION")
app.geometry("1600x600")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
button = ctk.CTkButton(master=app, text="Vote", command=index.cast_vote)

button.pack()
app.mainloop()
#
