from kivy.clock import Clock
from kivy.uix.button import Button


class MatchButton(Button):
    pass


class MatchButton(Button):
    all_buttons: list()
    pair_pending: MatchButton

    def get_other_half(self) -> MatchButton:
        pass

    def __set_other_half(self) -> None:
        pass

    def __set_symbol(self, symbol: str) -> None:
        pass


class MatchButton(Button):
    all_buttons: list() = list()
    pair_pending: MatchButton = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__other_half: MatchButton = None
        self.flipped: bool = False
        self.matched: bool = False

        self.symbol: str = None

        self.background_disabled_normal = self.background_normal
        self.disabled_color = self.color

        MatchButton.all_buttons.append(self)

    def get_other_half(self) -> MatchButton:
        return self.__other_half

    def set_other_half(self, value: MatchButton) -> None:
        self.__other_half = value

    def __set_symbol(self, symbol: str) -> None:
        self.symbol = symbol

    def on_press(self):
        super().on_press()

        self.flipped = True
        self.disabled = True
        self.background_color = "blue"
        self.text = self.symbol

        if MatchButton.pair_pending is not None:
            if MatchButton.pair_pending is not None and self.__other_half.flipped:
                self.on_good_match(self.__other_half)
                self.matched = True
                MatchButton.pair_pending.matched = True
            else:
                self.on_bad_match(MatchButton.pair_pending)

            MatchButton.pair_pending = None
            self.on_match_finish(self.__other_half)
        else:
            MatchButton.pair_pending = self

    def on_good_match(self, other):
        self.background_color = "green"
        other.background_color = "green"
        for button in self.all_buttons:
            button.disabled = True

        other.matched = True
        self.matched = True

        Clock.schedule_once(lambda _: MatchButton.reenable_buttons(self), 1)

    def on_bad_match(self, other):
        self.background_color = "red"
        other.background_color = "red"

        for button in self.all_buttons:
            button.disabled = True

        Clock.schedule_once(lambda _: MatchButton.reenable_buttons(self), 1)


    def on_match_finish(self, other):
        self.flipped = False
        other.flipped = False
        self.pair_pending = False
        other.pair_pending = False

    @staticmethod
    def associate(a: MatchButton, b: MatchButton, symbol: str):
        a.__set_symbol(symbol)
        b.__set_symbol(symbol)

        a.set_other_half(b)
        b.set_other_half(a)

    @staticmethod
    def reenable_buttons(instance: MatchButton):
        for button in MatchButton.all_buttons:
            if not button.matched:
                button.disabled = False
                button.background_color = [1, 1, 1, 1]
                button.text = ""


