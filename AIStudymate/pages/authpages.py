import reflex as rx
from ..styles.styles import dark_theme
def login_page():
    return rx.box(
        rx.heading("Login", size="xl", color=dark_theme["text_color"], mb="4"),
        rx.input(placeholder="Username", bg=dark_theme["input_background"], color=dark_theme["text_color"], border_color=dark_theme["input_border"], mb="4"),
        rx.input(placeholder="Password", type="password", bg=dark_theme["input_background"], color=dark_theme["text_color"], border_color=dark_theme["input_border"], mb="4"),
        rx.button("Login", bg=dark_theme["button_background"], hover_bg=dark_theme["button_hover"], color=dark_theme["text_color"], mb="4"),
        rx.text("Don't have an account?", color=dark_theme["text_color"]),
        rx.link("Signup", href="/signup", color=dark_theme["text_color"], mb="4"),
        display="flex",
        flex_direction="column",
        align_items="center",
        justify_content="center",
        height="100vh",
        bg=dark_theme["background"],
    )
def signup_page():
    return rx.box(
        rx.heading("Signup", size="xl", color=dark_theme["text_color"], mb="4"),
        rx.input(placeholder="Username", bg=dark_theme["input_background"], color=dark_theme["text_color"], border_color=dark_theme["input_border"], mb="4"),
        rx.input(placeholder="Email", bg=dark_theme["input_background"], color=dark_theme["text_color"], border_color=dark_theme["input_border"], mb="4"),
        rx.input(placeholder="Password", type="password", bg=dark_theme["input_background"], color=dark_theme["text_color"], border_color=dark_theme["input_border"], mb="4"),
        rx.button("Signup", bg=dark_theme["button_background"], hover_bg=dark_theme["button_hover"], color=dark_theme["text_color"], mb="4"),
        rx.text("Already have an account?", color=dark_theme["text_color"]),
        rx.link("Login", href="/login", color=dark_theme["text_color"]),
        display="flex",
        flex_direction="column",
        align_items="center",
        justify_content="center",
        height="100vh",
        bg=dark_theme["background"],
    )