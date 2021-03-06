from turtle import *
from config import Config
from menu_button import MenuButton


class Menu:
    buttons = []

    def draw(self, start_game_fun: callable):
        penup()
        setpos(Config.GAME_WIDTH / 2, Config.GAME_HEIGHT / 2)
        pendown()
        self.buttons.append(MenuButton('Hrát', start_game_fun, selected=True))
        self.buttons.append(MenuButton('Nastavení', self.show_settings))
        menu_start_y = (Config.GAME_HEIGHT - len(self.buttons) *
                        (Config.BUTTON_HEIGHT + Config.BUTTON_MARGIN) - Config.BUTTON_MARGIN) / 2
        for i in range(len(self.buttons)):
            self.buttons[i].start_pos = Config.GAME_WIDTH / 2 - Config.BUTTON_WIDTH / 2, menu_start_y + i * (
                Config.BUTTON_HEIGHT + Config.BUTTON_MARGIN) - Config.BUTTON_MARGIN
            self.buttons[i].draw()
        self.bind_events()

    def bind_events(self):
        onkey(self.on_enter, 'Return')
        onkey(self.select_upper_btn, 'Up')
        onkey(self.select_lower_btn, 'Down')
        listen()

    def remove_events(self):
        onkey(None, 'Return')
        onkey(None, 'Up')
        onkey(None, 'Down')

    def clear(self):
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
        index = self.get_selected_btn_index()
        self.buttons[index].on_enter()

    def show_settings(self):
        pass
