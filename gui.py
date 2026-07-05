import customtkinter as ctk
import tkinter as tk
import index
from PIL import Image  # pillow
import winsound

# --------------------------------------------------------------------------------------------------
window = ctk.CTk()
window.title("ELECTION")
window.geometry("1600x600")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
window.iconbitmap(r"assets\icon.ico")
# window.attributes("-fullscreen", True)
# --------------------------------------------------------------------------------------------------
party_img1 = ctk.CTkImage(
    light_image=Image.open(r"assets\party_logo.png"),
    dark_image=Image.open(r"assets\party_logo.png"),
    size=(150, 150),
)
party_img2 = ctk.CTkImage(
    light_image=Image.open(r"assets\party_logo.png"),
    dark_image=Image.open(r"assets\party_logo.png"),
    size=(150, 150),
)
party_img3 = ctk.CTkImage(
    light_image=Image.open(r"assets\party_logo.png"),
    dark_image=Image.open(r"assets\party_logo.png"),
    size=(150, 150),
)
party_img4 = ctk.CTkImage(
    light_image=Image.open(r"assets\party_logo.png"),
    dark_image=Image.open(r"assets\party_logo.png"),
    size=(150, 150),
)
# --------------------------------------------------------------------------------------------------
voting_frame = ctk.CTkFrame(window)
voting_frame.columnconfigure(0, weight=1)
voting_frame.columnconfigure(1, weight=1)
voting_frame.columnconfigure(2, weight=1)
voting_frame.columnconfigure(3, weight=1)

success_screen = ctk.CTkFrame(window)

content_frame = ctk.CTkFrame(
    success_screen,
    width=500,
    height=400,
    fg_color="transparent",
)
content_frame.pack(expand=True)
content_frame.pack_propagate(False)

tick_label = ctk.CTkLabel(
    content_frame,
    text="✔",
    font=("Segoe UI", 250, "bold"),
    text_color="green",
)

tick_label.pack()

success_label = ctk.CTkLabel(
    content_frame,
    text="Vote Cast Successfully",
    font=("Arial", 20, "bold"),
)

success_label.pack(pady=(10, 0))

party_img_label1 = ctk.CTkLabel(voting_frame, text="", image=party_img1)
party_img_label2 = ctk.CTkLabel(voting_frame, text="", image=party_img2)
party_img_label3 = ctk.CTkLabel(voting_frame, text="", image=party_img3)
party_img_label4 = ctk.CTkLabel(voting_frame, text="", image=party_img4)


# --------------------------------------------------------------------------------------------------
def vote_handler(party_name):
    disable_buttons()
    success, error = index.cast_vote(party_name)
    if success:
        play_success_sound()
        voting_frame.pack_forget()
        success_screen.pack(fill="both", expand=True)
        tick_label.configure(font=("Segoe UI", 10, "bold"))
        animate_tick(10)
        window.after(10000, show_voting_screen)
    else:
        error_label = ctk.CTkLabel(
            window, text=f"Error: {error}", font=("Arial", 20, "bold"), text_color="red"
        )
        error_label.pack(pady=20)


def show_voting_screen():
    success_screen.pack_forget()
    enable_buttons()
    voting_frame.pack(fill="x", padx=30, pady=400)


def play_success_sound():
    winsound.PlaySound(
        r"assets\success.wav", winsound.SND_FILENAME | winsound.SND_ASYNC
    )


def disable_buttons():
    button_1.configure(state="disabled")
    button_2.configure(state="disabled")
    button_3.configure(state="disabled")
    button_4.configure(state="disabled")


def enable_buttons():
    button_1.configure(state="normal")
    button_2.configure(state="normal")
    button_3.configure(state="normal")
    button_4.configure(state="normal")


def animate_tick(size):
    if size < 250:
        tick_label.configure(font=("Segoe UI", size, "bold"))
        success_screen.after(16, lambda: animate_tick(size + 20))
    else:
        tick_label.configure(font=("Segoe UI", 265, "bold"))
        success_screen.after(60, lambda: settle_tick())


def settle_tick():
    tick_label.configure(font=("Segoe UI", 250, "bold"))


# --------------------------------------------------------------------------------------------------
button_1 = ctk.CTkButton(
    master=voting_frame,
    text="Vote for party 1",
    font=("Arial", 20, "bold"),
    height=40,
    corner_radius=20,
    command=lambda: vote_handler("party1"),
)

button_2 = ctk.CTkButton(
    master=voting_frame,
    text="Vote for party 2",
    font=("Arial", 20, "bold"),
    height=40,
    corner_radius=20,
    command=lambda: vote_handler("party2"),
)

button_3 = ctk.CTkButton(
    master=voting_frame,
    text="Vote for party 3",
    font=("Arial", 20, "bold"),
    height=40,
    corner_radius=20,
    command=lambda: vote_handler("party3"),
)

button_4 = ctk.CTkButton(
    master=voting_frame,
    text="Vote for party 4",
    font=("Arial", 20, "bold"),
    height=40,
    corner_radius=20,
    command=lambda: vote_handler("party4"),
)
# --------------------------------------------------------------------------------------------------
button_1.grid(row=1, column=0, padx=60, sticky="ew")
button_2.grid(row=1, column=1, padx=60, sticky="ew")
button_3.grid(row=1, column=2, padx=60, sticky="ew")
button_4.grid(row=1, column=3, padx=60, sticky="ew")
party_img_label1.grid(row=0, column=0, pady=20)
party_img_label2.grid(row=0, column=1, pady=20)
party_img_label3.grid(row=0, column=2, pady=20)
party_img_label4.grid(row=0, column=3, pady=20)
show_voting_screen()
window.mainloop()
