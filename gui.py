# --------------------------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------------------------
import customtkinter as ctk
import tkinter as tk
import index
from PIL import Image  # pillow
import winsound
from GUI_constants import *

# --------------------------------------------------------------------------------------------------
# Window creation and config
# --------------------------------------------------------------------------------------------------
window = ctk.CTk()
window.title(window_title)
window.geometry(window_size)
ctk.set_appearance_mode(appearance_mode)
ctk.set_default_color_theme(color_theme)
window.iconbitmap(icon_path)
# window.attributes("-fullscreen", True)

# --------------------------------------------------------------------------------------------------
# Settings
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Assets
# --------------------------------------------------------------------------------------------------
school_logo = ctk.CTkImage(
    light_image=Image.open(school_logo_path),
    dark_image=Image.open(school_logo_path),
    size=school_logo_size,
)
party_img1 = ctk.CTkImage(
    light_image=Image.open(party_logo_path),
    dark_image=Image.open(party_logo_path),
    size=party_logo_size,
)
party_img2 = ctk.CTkImage(
    light_image=Image.open(party_logo_path),
    dark_image=Image.open(party_logo_path),
    size=party_logo_size,
)
party_img3 = ctk.CTkImage(
    light_image=Image.open(party_logo_path),
    dark_image=Image.open(party_logo_path),
    size=party_logo_size,
)
party_img4 = ctk.CTkImage(
    light_image=Image.open(party_logo_path),
    dark_image=Image.open(party_logo_path),
    size=party_logo_size,
)

animation_frames = []
animation_delays = []
tick_image = Image.open(success_checkmark_path)
for i in range(tick_image.n_frames):
    tick_image.seek(i)
    delay = tick_image.info.get("duration", default_animation_delay)
    animation_frames.append(
        ctk.CTkImage(
            light_image=tick_image.copy(),
            dark_image=tick_image.copy(),
            size=tick_animation_size,
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
    width=content_frame_width,
    height=content_frame_height,
    fg_color=transparent_color,
)

# frame configs
voting_frame.columnconfigure(0, weight=1)
voting_frame.columnconfigure(1, weight=1)
voting_frame.columnconfigure(2, weight=1)
voting_frame.columnconfigure(3, weight=1)

content_frame.pack(expand=True)
content_frame.pack_propagate(False)

# labels
school_logo_label = ctk.CTkLabel(
    window,
    image=school_logo,
    text="",
    fg_color=transparent_color,
)
title_label = ctk.CTkLabel(
    window,
    text=title_text,
    font=title_font,
    text_color=brand_purple,
)
tick_label = ctk.CTkLabel(
    content_frame,
    text="",
    image=animation_frames[0],
)
tick_label.animation_frames = animation_frames
tick_label.pack()

success_label = ctk.CTkLabel(
    content_frame,
    text=vote_success_text,
    font=heading_font,
)

success_label.pack(pady=(10, 0))

party_name_label_1 = ctk.CTkLabel(
    voting_frame,
    text=party_1_name,
    font=heading_font,
    text_color=light_text_color,
)
party_name_label_2 = ctk.CTkLabel(
    voting_frame,
    text=party_2_name,
    font=heading_font,
    text_color=light_text_color,
)
party_name_label_3 = ctk.CTkLabel(
    voting_frame,
    text=party_3_name,
    font=heading_font,
    text_color=light_text_color,
)
party_name_label_4 = ctk.CTkLabel(
    voting_frame,
    text=party_4_name,
    font=heading_font,
    text_color=light_text_color,
)

party_slogan_label_1 = ctk.CTkLabel(
    voting_frame,
    text=party_1_slogan,
    font=subheading_font,
    text_color=light_secondary_text_color,
)
party_slogan_label_2 = ctk.CTkLabel(
    voting_frame,
    text=party_2_slogan,
    font=subheading_font,
    text_color=light_secondary_text_color,
)
party_slogan_label_3 = ctk.CTkLabel(
    voting_frame,
    text=party_3_slogan,
    font=subheading_font,
    text_color=light_secondary_text_color,
)
party_slogan_label_4 = ctk.CTkLabel(
    voting_frame,
    text=party_4_slogan,
    font=subheading_font,
    text_color=light_secondary_text_color,
)

party_img_label1 = ctk.CTkLabel(voting_frame, text="", image=party_img1)
party_img_label2 = ctk.CTkLabel(voting_frame, text="", image=party_img2)
party_img_label3 = ctk.CTkLabel(voting_frame, text="", image=party_img3)
party_img_label4 = ctk.CTkLabel(voting_frame, text="", image=party_img4)

# buttons
button_1 = ctk.CTkButton(
    master=voting_frame,
    text=party_1_button_text,
    font=heading_font,
    width=button_width,
    height=button_height,
    corner_radius=button_corner_radius,
    fg_color=primary_button_color,
    hover_color=primary_button_hover_color,
    text_color="white",
    border_width=0,
    command=lambda: vote_handler("party1"),
)

button_2 = ctk.CTkButton(
    master=voting_frame,
    text=party_2_button_text,
    font=heading_font,
    width=button_width,
    height=button_height,
    corner_radius=button_corner_radius,
    fg_color=primary_button_color,
    hover_color=primary_button_hover_color,
    text_color="white",
    border_width=0,
    command=lambda: vote_handler("party2"),
)

button_3 = ctk.CTkButton(
    master=voting_frame,
    text=party_3_button_text,
    font=heading_font,
    width=button_width,
    height=button_height,
    corner_radius=button_corner_radius,
    fg_color=primary_button_color,
    hover_color=primary_button_hover_color,
    text_color="white",
    border_width=0,
    command=lambda: vote_handler("party3"),
)

button_4 = ctk.CTkButton(
    master=voting_frame,
    text=party_4_button_text,
    font=heading_font,
    width=button_width,
    height=button_height,
    corner_radius=button_corner_radius,
    fg_color=primary_button_color,
    hover_color=primary_button_hover_color,
    text_color="white",
    border_width=0,
    command=lambda: vote_handler("party4"),
)


# --------------------------------------------------------------------------------------------------
# Function defs
# --------------------------------------------------------------------------------------------------
def vote_handler(party_name):
    disable_buttons()
    success, error_from_fun_call = index.cast_vote(party_name)
    if success:
        play_success_sound()
        voting_frame.pack_forget()
        success_screen_frame.pack(fill="both", expand=True)
        tick_label.configure(image=animation_frames[0])
        play_tick_animation()
        window.after(success_screen_duration, show_voting_screen)
    else:
        error_label = ctk.CTkLabel(
            window,
            text=f"Error: {error_from_fun_call}",
            font=heading_font,
            text_color=error_color,
        )
        error_label.pack(pady=20)


def show_voting_screen():
    success_screen_frame.pack_forget()
    school_logo_label.pack(
        pady=(spacing_24, spacing_16),
    )
    title_label.pack()
    enable_buttons()
    voting_frame.pack(
        fill="x",
        padx=voting_frame_padx,
        pady=voting_frame_pady,
    )


def play_success_sound():
    winsound.PlaySound(
        success_sound_path,
        winsound.SND_FILENAME | winsound.SND_ASYNC,
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
party_img_label1.grid(row=0, column=0, pady=(12, 7))
party_img_label2.grid(row=0, column=1, pady=(12, 7))
party_img_label3.grid(row=0, column=2, pady=(12, 7))
party_img_label4.grid(row=0, column=3, pady=(12, 7))
party_name_label_1.grid(row=1, column=0, pady=(0, 4))
party_name_label_2.grid(row=1, column=1, pady=(0, 4))
party_name_label_3.grid(row=1, column=2, pady=(0, 4))
party_name_label_4.grid(row=1, column=3, pady=(0, 4))
party_slogan_label_1.grid(row=2, column=0, pady=(0, 10))
party_slogan_label_2.grid(row=2, column=1, pady=(0, 10))
party_slogan_label_3.grid(row=2, column=2, pady=(0, 10))
party_slogan_label_4.grid(row=2, column=3, pady=(0, 10))
button_1.grid(row=4, column=0, padx=60, sticky="ew")
button_2.grid(row=4, column=1, padx=60, sticky="ew")
button_3.grid(row=4, column=2, padx=60, sticky="ew")
button_4.grid(row=4, column=3, padx=60, sticky="ew")

# --------------------------------------------------------------------------------------------------
# Application startup
# --------------------------------------------------------------------------------------------------
show_voting_screen()
window.mainloop()
