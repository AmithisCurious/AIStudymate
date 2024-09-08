import reflex as rx
from .styles import style

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
            bg="transparent",  # Make the background transparent
            color="#FFFFFF",  # White text for contrast
            padding="1em",
            border_radius="0.5em",
            max_width="60%",
            align_self="flex-end",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
            bg="transparent",  # Make the background transparent
            color="#A5B4FC",  # Light blue text for answers
            padding="1em",
            border_radius="0.5em",
            max_width="60%",
            align_self="flex-start",
        ),
        margin_y="1em",
        width="100%",
    )


def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ],
        padding="4em",
        overflow_y="auto",  # Scrollable chat area
        flex="1",  # Allow chat to take available space
        bg="#1F2937",  # Dark background for chat area
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question...",
            style=style.input_style,
            width="85%",  # Make the input take most of the width
            padding="0.2em",  # Adjusted padding to ensure no text cutting
            font_size="1.1em",
            color="#FFFFFF",
            bg="#2E3B55",  # Dark background for input box
            border="1px solid #4B5563",
            border_radius="0.5em",
            line_height="1.0em",  # Set line height to prevent text cutting
            height="2.0em",  # Increase height slightly to avoid clipping
        ),
        rx.button(
            "Send", 
            style=style.button_style,
            padding="0.4em",
            width="10%",
            bg="#4F46E5",
            color="#FFFFFF",
            hover_bg="#7C3AED",
            border_radius="0.5em",
        ),
        justify="space-between",
        padding="1em",
        width="100%",
        bg="#111827",  # Dark background for action bar
        border_top="1px solid #4B5563",  # Add subtle border to separate action bar
    )


def index() -> rx.Component:
    return rx.vstack(
        chat(),
        action_bar(),
        spacing="0",  # No space between chat and action bar
        height="100vh",  # Full height of the viewport
        width="100vw",  # Full width of the viewport
        overflow="hidden",  # Prevent scrollbars from appearing
        align_items="stretch",  # Ensure full-width alignment
    )


app = rx.App()
app.add_page(index)
