from turtle import Vec2D, onkey, listen, done
from app_config import AppConfig


class Menu:

    def __init__(self, center: Vec2D, buttons: list, is_vertical: bool):
        self.buttons = buttons
        self.is_vertical = is_vertical
        if is_vertical:
            self.start_pos = (center[0] - AppConfig.BUTTON_WIDTH / 2, center[1] - len(
                buttons) / 2 * (AppConfig.BUTTON_HEIGHT + AppConfig.BUTTON_MARGIN))
            if len(buttons) % 2 == 0:
                self.start_pos = (self.start_pos[0], self.start_pos[1] + AppConfig.BUTTON_MARGIN / 2)
            else:
                self.start_pos = (self.start_pos[0], self.start_pos[1] + AppConfig.BUTTON_HEIGHT / 2)
        else:
            self.start_pos = (center[1] - len(buttons) / 2 * (AppConfig.BUTTON_WIDTH +
                AppConfig.BUTTON_MARGIN), center[1] - AppConfig.BUTTON_HEIGHT / 2)
            if len(buttons) % 2 == 0:
                self.start_pos[0] -= AppConfig.BUTTON_MARGIN / 2
            else:
                self.start_pos[0] -= AppConfig.BUTTON_WIDTH / 2

    def draw(self):
        if self.is_vertical: self.draw_vertical()
        else: self.draw_horizontal()
        self.bind_events()
        done()

    def draw_horizontal(self):
        for i in range(len(self.buttons)):
            self.buttons[i].center = (AppConfig.GAME_WIDTH / 2, menu_start_y + i * (
                AppConfig.BUTTON_HEIGHT + AppConfig.BUTTON_MARGIN) - AppConfig.BUTTON_MARGIN)
            self.buttons[i].draw()

    def draw_vertical(self):
        for i in range(len(self.buttons)):
            self.buttons[i].start_pos = (self.start_pos[0], self.start_pos[1] + i * (
                AppConfig.BUTTON_HEIGHT + AppConfig.BUTTON_MARGIN) - AppConfig.BUTTON_MARGIN)
            self.buttons[i].draw()

    def bind_events(self):
        onkey(self.on_enter, 'Return')
        if self.is_vertical:
            onkey(self.select_upper_btn, 'Up')
            onkey(self.select_lower_btn, 'Down')
        else:
            onkey(self.select_upper_btn, 'Right')
            onkey(self.select_lower_btn, 'Left')
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
        index = self.get_selected_btn_index()
        if index == 0: return
        self.buttons[index].selected = False
        self.buttons[index].draw()
        self.buttons[index - 1].selected = True
        self.buttons[index - 1].draw()

    def select_lower_btn(self):
        index = self.get_selected_btn_index()
        if index == len(self.buttons) - 1: return
        self.buttons[index].selected = False
        self.buttons[index].draw()
        self.buttons[index + 1].selected = True
        self.buttons[index + 1].draw()

    def on_enter(self):
        self.clear()
        index = self.get_selected_btn_index()
        self.buttons[index].on_enter()
