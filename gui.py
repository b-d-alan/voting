# --------------------------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------------------------
import customtkinter as ctk
import tkinter as tk
import index
from PIL import Image  # pillow
import winsound

# --------------------------------------------------------------------------------------------------
# Window creation and config
# --------------------------------------------------------------------------------------------------
window = ctk.CTk()
window.title("ELECTION")
window.geometry("1600x600")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
window.iconbitmap(r"assets\icon.ico")
# window.attributes("-fullscreen", True)

# --------------------------------------------------------------------------------------------------
# Settings
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Assets
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

animation_frames = []
animation_delays = []
tick_image = Image.open(r"assets\success_checkmark.png")
for i in range(tick_image.n_frames):
    tick_image.seek(i)
    delay = tick_image.info.get("duration", 33)
    animation_frames.append(
        ctk.CTkImage(
            light_image=tick_image.copy(),
            dark_image=tick_image.copy(),
            size=(220, 220),
        )
    )
    animation_delays.append(delay)

# --------------------------------------------------------------------------------------------------
# Widget creation
# --------------------------------------------------------------------------------------------------
# frames
voting_frame = ctk.CTkFrame(window)
success_screen_frame = ctk.CTkFrame(window)
content_frame = ctk.CTkFrame(
    success_screen_frame,
    width=500,
    height=400,
    fg_color="transparent",
)

# frame configs
voting_frame.columnconfigure(0, weight=1)
voting_frame.columnconfigure(1, weight=1)
voting_frame.columnconfigure(2, weight=1)
voting_frame.columnconfigure(3, weight=1)

content_frame.pack(expand=True)
content_frame.pack_propagate(False)

# labels
tick_label = ctk.CTkLabel(
    content_frame,
    text="",
    image=animation_frames[0],
)
tick_label.animation_frames = animation_frames
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

# buttons
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
# Function defs
# --------------------------------------------------------------------------------------------------
def vote_handler(party_name):
    disable_buttons()
    success, error = index.cast_vote(party_name)
    if success:
        play_success_sound()
        voting_frame.pack_forget()
        success_screen_frame.pack(fill="both", expand=True)
        tick_label.configure(image=animation_frames[0])
        play_tick_animation()
        window.after(10000, show_voting_screen)
    else:
        error_label = ctk.CTkLabel(
            window, text=f"Error: {error}", font=("Arial", 20, "bold"), text_color="red"
        )
        error_label.pack(pady=20)


def show_voting_screen():
    success_screen_frame.pack_forget()
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


def play_tick_animation(frame=0):
    tick_label.configure(image=animation_frames[frame])

    if frame < len(animation_frames) - 1:
        delay = int(animation_delays[frame])
        success_screen_frame.after(
            delay,
            lambda: play_tick_animation(frame + 1),
        )


# --------------------------------------------------------------------------------------------------
# Widget layout
# --------------------------------------------------------------------------------------------------
button_1.grid(row=1, column=0, padx=60, sticky="ew")
button_2.grid(row=1, column=1, padx=60, sticky="ew")
button_3.grid(row=1, column=2, padx=60, sticky="ew")
button_4.grid(row=1, column=3, padx=60, sticky="ew")
party_img_label1.grid(row=0, column=0, pady=20)
party_img_label2.grid(row=0, column=1, pady=20)
party_img_label3.grid(row=0, column=2, pady=20)
party_img_label4.grid(row=0, column=3, pady=20)

# --------------------------------------------------------------------------------------------------
# Application startup
# --------------------------------------------------------------------------------------------------
show_voting_screen()
window.mainloop()
