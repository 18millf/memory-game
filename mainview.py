from kivy.uix.gridlayout import GridLayout

class MainView(GridLayout):
    def __init__(self, rows: int, columns: int, **kwargs) -> None:
        super().__init__(**kwargs)

        cells = rows * columns

        # cant have pairs if there are an odd number of cells
        assert cells % 2 == 0

        self.cols = columns

        for _ in range(rows * columns):
            


