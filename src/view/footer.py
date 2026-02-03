from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Footer


class FooterWidget(Widget):
    """Custom Footer Widget for the application."""

    def compose(self) -> ComposeResult:
        yield Footer(show_command_palette=False)
