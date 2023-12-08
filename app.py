from kivy.app import App
from kivy.uix.widget import Widget

from mainview import MainView


COLUMNS = 5
ROWS = 4


class Application(App):
    def build(self) -> Widget:
        self.root = MainView(ROWS, COLUMNS)
        return self.root