from textual.app import App
from textual.binding import Binding
from .footer import FooterWidget
from .header import HeaderWidget


class KesherMenu(App):

    BINDINGS = [
        Binding(key="s", action="stop", description="Stop"),
        Binding(key="r", action="restart", description="Restart"),
        Binding(key="q", action="quit", description="Quit"),
    ]

    def compose(self):
        yield HeaderWidget()
        yield FooterWidget()
