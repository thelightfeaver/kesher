from textual.app import ComposeResult
from textual.widgets import Header


class HeaderWidget(Header):
    """Custom Header Widget for the application."""

    def compose(self) -> ComposeResult:
        yield Header()
