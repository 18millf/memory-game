from kivy.uix.gridlayout import GridLayout
from matchbutton import MatchButton
from random import shuffle

class MainView(GridLayout):
    SYMBOLS: str = "QWERTYUIOPASDFGHJKLZXCVBNM"

    def __init__(self, rows: int, columns: int, **kwargs) -> None:
        super().__init__(**kwargs)

        cells = rows * columns

        # cant have pairs if there are an odd number of cells
        assert cells % 2 == 0

        self.cols = columns
        self.__buttons: list[MatchButton] = list()

        for _ in range(cells):
            button: MatchButton = MatchButton()
            self.__buttons.append(button)

        shuffle(self.__buttons)

        for i in range(0, cells, 2):
            button_a: MatchButton = self.__buttons[i]
            button_b: MatchButton = self.__buttons[i + 1]

            MatchButton.associate(button_a, button_b, MainView.SYMBOLS[i // 2])