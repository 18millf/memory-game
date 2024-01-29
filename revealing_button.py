from kivy.clock import Clock
from kivy.uix.button import Button


class RevealingButton(Button):
    def __init__(self, row: int, col: int, value: int, **kwargs):
        super().__init__(**kwargs)

        # this needs to be imported in the functions where its used otherwise a circular dependency is created
        from button_grid import ButtonGrid

        self.parent: ButtonGrid

        self.row: int = row
        self.col: int = col
        self.value: str = str(value)

    def show(self):
        self.text = self.value
        self.disabled = True

    def hide(self):
        self.text = ""
        self.disabled = False

    def hide_schedule_callback(self, other):
        from button_grid import ButtonGrid
        self.parent: ButtonGrid

        self.hide()
        other.hide()

        self.parent.first_clicked = None
        self.parent.second_clicked = None

    def on_press(self, *args):
        from button_grid import ButtonGrid
        self.parent: ButtonGrid

        if (self.parent.revealed[self.col][self.row] or
                self.parent.first_clicked == (self.col, self.row) or
                self.parent.second_clicked is not None):
            return

        if self.parent.first_clicked is None:
            self.parent.first_clicked = (self.col, self.row)
            self.show()

        else:
            other_button_coords: (int, int) = self.parent.first_clicked
            other_button: RevealingButton = self.parent.buttons[other_button_coords[0]][other_button_coords[1]]

            if self.value == other_button.value:
                self.parent.revealed[self.col][self.row] = True
                self.parent.revealed[other_button.col][other_button.row] = True

                self.parent.first_clicked = None
                self.parent.second_clicked = None

                all_revealed = True
                for row in self.parent.revealed:
                    for val in row:
                        if not val:
                            all_revealed = False
                            break
                    if not all_revealed:
                        break

                if all_revealed:
                    self.parent.parent.ids["status_test"].text = "You win!"

            else:
                Clock.schedule_once(lambda _: self.hide_schedule_callback(other_button), 2)
