# --------------------------------------------------------------------------------------------------
# Appearance
# --------------------------------------------------------------------------------------------------

appearance_mode = "light"  # "light", "dark", "system"
color_theme = "blue"

# --------------------------------------------------------------------------------------------------
# Window
# --------------------------------------------------------------------------------------------------

window_title = "ELECTION"

window_width = 1600
window_height = 600
window_size = f"{window_width}x{window_height}"

minimum_window_width = 1200
minimum_window_height = 700

# --------------------------------------------------------------------------------------------------
# Typography
# --------------------------------------------------------------------------------------------------

font_family = "Segoe UI"

title_font = (font_family, 36, "bold")
heading_font = (font_family, 32, "bold")
subheading_font = (font_family, 27, "bold")
body_font = (font_family, 15)
small_font = (font_family, 13)

# --------------------------------------------------------------------------------------------------
# Brand colours
# --------------------------------------------------------------------------------------------------

brand_purple = "#33208D"
brand_purple_hover = "#442AA8"
brand_purple_pressed = "#27176F"
brand_purple_light = "#ECE9FB"

brand_green = "#22C55E"
brand_green_hover = "#16A34A"
brand_green_pressed = "#15803D"
brand_green_disabled = "#A7DDBA"

# --------------------------------------------------------------------------------------------------
# Light theme
# --------------------------------------------------------------------------------------------------

light_background_color = "#F7F8FC"
light_secondary_background_color = "#EEF1F7"

light_card_color = "#FFFFFF"
light_elevated_card_color = "#FCFCFE"

light_text_color = "#171717"
light_secondary_text_color = "#5D6472"
light_placeholder_text_color = "#8A92A3"
light_disabled_text_color = "#B2B7C2"

light_border_color = "#D8DCE8"
light_divider_color = "#E8EBF2"
light_focus_color = "#7C68E8"

# --------------------------------------------------------------------------------------------------
# Dark theme
# --------------------------------------------------------------------------------------------------

dark_background_color = "#12141D"
dark_secondary_background_color = "#181C27"

dark_card_color = "#1E2431"
dark_elevated_card_color = "#252C3C"

dark_text_color = "#F8F9FC"
dark_secondary_text_color = "#B9C0CF"
dark_placeholder_text_color = "#8991A3"

dark_border_color = "#30384A"
dark_divider_color = "#282E3E"
dark_focus_color = "#8E7EFF"

# --------------------------------------------------------------------------------------------------
# Component colours
# --------------------------------------------------------------------------------------------------

# Buttons
primary_button_color = brand_green
primary_button_hover_color = brand_green_hover
primary_button_pressed_color = brand_green_pressed

secondary_button_color = brand_purple_light
secondary_button_hover_color = "#E3E8FF"
secondary_button_pressed_color = "#D5DCFF"

# Status
success_color = "#22C55E"
warning_color = "#F59E0B"
error_color = "#DC2626"
information_color = "#3B82F6"

# Miscellaneous
transparent_color = "transparent"

# --------------------------------------------------------------------------------------------------
# Component sizes
# --------------------------------------------------------------------------------------------------

# General
frame_corner_radius = 12

# Buttons
button_width = 250
button_height = 50
button_corner_radius = 10

# Entries
entry_corner_radius = 10
entry_border_width = 1

# Images
party_logo_size = (200, 200)
school_logo_size = (562.5, 150)
tick_animation_size = (220, 220)

# Frames
content_frame_width = 500
content_frame_height = 400

# --------------------------------------------------------------------------------------------------
# Layout & spacing
# --------------------------------------------------------------------------------------------------

spacing_4 = 4
spacing_8 = 8
spacing_16 = 16
spacing_24 = 24
spacing_32 = 32
spacing_48 = 48

voting_frame_padx = 30
voting_frame_pady = 200

# --------------------------------------------------------------------------------------------------
# Animation & timing
# --------------------------------------------------------------------------------------------------

hover_animation_ms = 150
default_animation_delay = 33
success_screen_duration = 10000

# --------------------------------------------------------------------------------------------------
# Assets
# --------------------------------------------------------------------------------------------------

icon_path = r"assets\icon.ico"

logo_path = r"assets\logo.png"
school_logo_path = r"assets\school_logo.png"
# background_path = r"assets\KerenSchoolFrontView.jpeg"
background_path = r"assets\background gradient.jpeg"
party_1_logo_path = r"assets\alpha party img.jpeg"
party_2_logo_path = r"assets\Keren students voice img.jpeg"
party_3_logo_path = r"assets\shalom kerenite party img.jpeg"

success_checkmark_path = r"assets\success_checkmark.png"
success_sound_path = r"assets\success.wav"

# --------------------------------------------------------------------------------------------------
# Application text
# --------------------------------------------------------------------------------------------------

vote_success_text = "Vote recorded successfully"

title_text = "Mock Election 2026"

party_1_button_text = "Vote"
party_2_button_text = "Vote"
party_3_button_text = "Vote"

party_1_name = "Alpha party"
party_2_name = "Keren students voice"
party_3_name = "Shalom Kerenite party"
