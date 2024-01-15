from kivy.clock import Clock
from kivy.uix.button import Button


class MatchButton(Button):
    pass


class MatchButton(Button):
    all_buttons: list[MatchButton]


class MatchButton(Button):
    all_buttons: list[MatchButton] = list()
    working_pair: (MatchButton, MatchButton) = (None, None)

    def __init__(self, symbol: str, **kwargs):
        super().__init__(**kwargs)

        MatchButton.all_buttons.append(self)
        
        self.symbol = symbol

    def on_press(self):
        button_a, _ = MatchButton.working_pair
        self.background_color = "blue"

        self.show_symbol()

        if button_a == None:
            MatchButton.working_pair = (self, None)
        else:
            for button in MatchButton.all_buttons:
                button.disabled = True

            MatchButton.working_pair = (button_a, self)

            a, b = MatchButton.working_pair

            if MatchButton.is_match(MatchButton.working_pair):
                MatchButton.buttons_matched(a, b)
            else:
                MatchButton.buttons_not_mached(a, b)

            if MatchButton.working_pair[0] != None and MatchButton.working_pair[1] != None:
                MatchButton.schedule_hide(MatchButton.working_pair)

                for button in MatchButton.all_buttons:
                    button.disabled = True

        return super().on_press()
    
    def show_symbol(self):
        self.text = self.symbol

    def hide_symbol(self):
        self.text = ""

    def schedule_hide(pair: (MatchButton, MatchButton)):
        Clock.schedule_once(lambda _: MatchButton.hide_symbols_if_no_match(pair), 1)
    
    def hide_symbols_if_no_match(pair: (MatchButton, MatchButton)):
        a, b = pair

        a.hide_symbol()
        b.hide_symbol()

        a.background_color = "white"
        b.background_color = "white"

        for button in MatchButton.all_buttons:
            button.disabled = False
                    
        if MatchButton.is_match((a, b)):
            a, b = MatchButton.working_pair
            a.disabled = True
            b.disabled = True

            a.show_symbol()
            b.show_symbol()

            a.background_color = "lime"
            b.background_color = "lime"
            
            MatchButton.working_pair = (None, None)
        elif a != None and b != None:
            MatchButton.working_pair = (None, None)


    @staticmethod
    def is_match(pair: (MatchButton, MatchButton)) -> bool:
        a, b = pair

        return a.symbol == b.symbol
    
    @staticmethod
    def buttons_matched(a: MatchButton, b: MatchButton):
        a.background_color = "lime"
        b.background_color = "lime"

    @staticmethod
    def buttons_not_mached(a: MatchButton, b: MatchButton):
        a.background_color = "red"
        b.background_color = "red"

    

