from kivy.clock import Clock
from kivy.uix.button import Button


class RevealingButton(Button):
    def __init__(self, row: int, col: int, value: int, **kwargs):
        super().__init__(**kwargs)

        self.row: int = row
        self.col: int = col
        self.value: str = str(value)

        self.show()
        Clock.schedule_once(lambda dt: self.hide(), 10)

    def show(self):
        self.text = self.value
        self.disabled = True

    def hide(self):
        self.text = ""
        self.disabled = False
