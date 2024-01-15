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

        for i in range(0, cells, 2):
            button_a: MatchButton = MatchButton(MainView.SYMBOLS[i // 2])
            button_b: MatchButton = MatchButton(MainView.SYMBOLS[i // 2])

            self.__buttons.append(button_a)
            self.__buttons.append(button_b)

        shuffle(self.__buttons)

        for button in self.__buttons:
            self.add_widget(button)
