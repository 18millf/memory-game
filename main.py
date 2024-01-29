from kivy.app import App

from game_window import *
from button_grid import *
from revealing_button import *


class MemoryGameApp(App):
    def build(self):
        return GameWindow()


app: App = MemoryGameApp()
app.run()
