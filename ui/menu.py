from turtle import Vec2D, onkey, listen, done
from app_config import AppConfig


class Menu:

    def __init__(self, center: Vec2D, buttons: list, is_vertical: bool, exit_on_enter: bool = True, button_width: int = AppConfig.BUTTON_WIDTH, button_height: int = AppConfig.BUTTON_HEIGHT):
        self.buttons = buttons
        self.is_vertical = is_vertical
        self.exit_on_enter = exit_on_enter
        self.button_width = button_width
        self.button_height = button_height
        if is_vertical:
            self.start_pos = (center[0] - button_width / 2, center[1] - len(
                buttons) / 2 * (button_height + AppConfig.BUTTON_MARGIN))
            if len(buttons) % 2 == 0:
                self.start_pos = (self.start_pos[0], self.start_pos[1] + AppConfig.BUTTON_MARGIN / 2)
            else:
                self.start_pos = (self.start_pos[0], self.start_pos[1] + button_height / 2)
        else:
            self.start_pos = (center[0] - len(buttons) / 2 * (button_width +
                AppConfig.BUTTON_MARGIN), center[1] - button_height / 2)
            if len(buttons) % 2 == 0:
                self.start_pos = (self.start_pos[0] - AppConfig.BUTTON_MARGIN / 2, self.start_pos[1])
            else:
                self.start_pos = (self.start_pos[0] - button_width / 2, self.start_pos[1])

    def draw(self):
        if self.is_vertical: self.draw_vertical()
        else: self.draw_horizontal()
        self.bind_events()
        done()

    def draw_horizontal(self):
        for i in range(len(self.buttons)):
            self.buttons[i].start_pos = (self.start_pos[0] + i * (self.button_width + AppConfig.BUTTON_MARGIN) - AppConfig.BUTTON_MARGIN, self.start_pos[1])
            self.buttons[i].draw()

    def draw_vertical(self):
        for i in range(len(self.buttons)):
            self.buttons[i].start_pos = (self.start_pos[0], self.start_pos[1] + i * (
                self.button_height + AppConfig.BUTTON_MARGIN) - AppConfig.BUTTON_MARGIN)
            self.buttons[i].draw()

    def bind_events(self):
        onkey(self.on_enter, 'Return')
        if self.is_vertical:
            onkey(self.select_upper_btn, 'Up')
            onkey(self.select_lower_btn, 'Down')
        else:
            onkey(self.select_lower_btn, 'Right')
            onkey(self.select_upper_btn, 'Left')
        listen()

    def remove_events(self):
        onkey(None, 'Return')
        onkey(None, 'Up')
        onkey(None, 'Down')
        onkey(None, 'Left')
        onkey(None, 'Right')

    def clear(self):
        self.remove_events()
        for btn in self.buttons:
            btn.clear()

    def get_selected_btn_index(self):
        selected = list(filter(lambda btn: (btn.selected), self.buttons))[0]
        return self.buttons.index(selected)

    def select_upper_btn(self):
        self.remove_events()
        index = self.get_selected_btn_index()
        self.buttons[index].selected = False
        self.buttons[index].draw()
        if index == 0:
            index = len(self.buttons)
        self.buttons[index - 1].selected = True
        self.buttons[index - 1].draw()
        self.bind_events()

    def select_lower_btn(self):
        self.remove_events()
        index = self.get_selected_btn_index()
        if index == len(self.buttons) - 1:
            index = -1
        self.buttons[index].selected = False
        self.buttons[index].draw()
        self.buttons[index + 1].selected = True
        self.buttons[index + 1].draw()
        self.bind_events()

    def on_enter(self):
        if self.exit_on_enter:
            self.clear()
        index = self.get_selected_btn_index()
        self.buttons[index].on_enter()
