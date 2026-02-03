from textual.widgets import Footer
from textual.app import ComposeResult
from textual.binding import Binding


class FooterWidget(Footer):
    """Custom Footer Widget for the application."""

    BINDINGS = [
        Binding(key="s", action="stop", description="Stop app"),
        Binding(key="r", action="restart", description="Restart app"),
        Binding(key="q", action="quit", description="Quit app"),
    ]

    def compose(self) -> ComposeResult:
        yield Footer()
