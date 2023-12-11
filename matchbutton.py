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
    pair_pending: MatchButton = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__other_half: MatchButton
        self.flipped: bool = False
        self.matched: bool = False

        MatchButton.all_buttons.append(self)

    def get_other_half(self) -> MatchButton:
        return self.__other_half
    
    def set_other_half(self, value: MatchButton) -> None:
        self.__other_half = value

    def __set_symbol(self, symbol: str) -> None:
        self.text = symbol

    def on_press(self):
        super().on_press()

        self.flipped = True

        if MatchButton.pair_pending != None:
            if MatchButton.pair_pending != None and self.__other_half.flipped:
                self.on_match(self.__other_half)
                self.matched = True
                MatchButton.pair_pending.matched = True
            else:
                self.on_bad_match(MatchButton.pair_pending)

            MatchButton.pair_pending = None
            self.on_match_finish(self.__other_half)
        else:
            MatchButton.pair_pending = self
        

    def on_good_match(self, other):
        pass

    def on_bad_match(self, other):
        pass

    def on_match_finish(self, other):
        pass
        
    @staticmethod
    def associate(a: MatchButton, b: MatchButton, symbol: str):
        a.__set_symbol(symbol)
        b.__set_symbol(symbol)

        a.__set_other_half(b)
        b.__set_other_half(a)