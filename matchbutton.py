from kivy.uix.button import Button

class MatchButton(Button):
    pass

class MatchButton(Button):
    def get_other_half(self) -> MatchButton:
        pass

    def __set_other_half(self) -> None:
        pass

    def __set_symbol(self, symbol: str) -> None:
        pass

class MatchButton(Button):
    all_buttons: list(MatchButton)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__other_half: MatchButton

        MatchButton.all_buttons.append(self)

    def get_other_half(self) -> MatchButton:
        return self.__other_half
    
    def set_other_half(self, value: MatchButton) -> None:
        self.__other_half = value

    def __set_symbol(self, symbol: str) -> None:
        self.text = symbol
        
    @staticmethod
    def associate(a: MatchButton, b: MatchButton, symbol: str):
        a.__set_symbol(symbol)
        b.__set_symbol(symbol)

        a.__set_other_half(b)
        b.__set_other_half(a)