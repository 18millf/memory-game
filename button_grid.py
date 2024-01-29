from kivy.uix.gridlayout import GridLayout
from random import shuffle

from revealing_button import RevealingButton

WIDTH: int = 5
HEIGHT: int = 4
AREA: int = WIDTH * HEIGHT


class ButtonGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        linear_values = [i // 2 + 1 for i in range(AREA)]
        shuffle(linear_values)
        self.values = [linear_values[i:i + WIDTH] for i in range(0, AREA, WIDTH)]

        for x in range(WIDTH):
            for y in range(HEIGHT):
                button: RevealingButton = RevealingButton(x, y, self.values[y][x])
                self.add_widget(button)
