from textual.app import App
from textual.widgets import Label

class KesherMenu(App):
    def compose(self):
        yield Label("Welcome to Kesher Menu")