from textual.app import App
from textual.binding import Binding
from .footer import FooterWidget
from .header import HeaderWidget


class KesherMenu(App):
    def compose(self):
        yield HeaderWidget()
        yield FooterWidget()
