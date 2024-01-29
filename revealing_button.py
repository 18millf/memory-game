from kivy.uix.button import Button


class RevealingButton(Button):
    def __init__(self, row: int, col: int, value: int, **kwargs):
        super().__init__(**kwargs)

        self.row: int = row
        self.col: int = col
        self.value: int = value

        self.text = str(value)
