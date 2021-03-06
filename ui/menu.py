from turtle import onkey, listen, done
from app_config import AppConfig
from .menu_button import MenuButton
from .settings import Settings
from game.main import Game


class Menu:
    buttons = []

    def draw(self):
        self.buttons.append(MenuButton('Hrát', self.start_game, selected=True))
        self.buttons.append(MenuButton('Nastavení', self.show_settings))
        menu_start_y = (AppConfig.GAME_HEIGHT - len(self.buttons) *
                        (AppConfig.BUTTON_HEIGHT + AppConfig.BUTTON_MARGIN) - AppConfig.BUTTON_MARGIN) / 2
        for i in range(len(self.buttons)):
            self.buttons[i].start_pos = AppConfig.GAME_WIDTH / 2 - AppConfig.BUTTON_WIDTH / 2, menu_start_y + i * (
                AppConfig.BUTTON_HEIGHT + AppConfig.BUTTON_MARGIN) - AppConfig.BUTTON_MARGIN
            self.buttons[i].draw()
        self.bind_events()
        done()

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
        if index == 0:
            return
        self.buttons[index].selected = False
        self.buttons[index].draw()
        self.buttons[index - 1].selected = True
        self.buttons[index - 1].draw()

    def select_lower_btn(self):
        index = self.get_selected_btn_index()
        if index == len(self.buttons) - 1:
            return
        self.buttons[index].selected = False
        self.buttons[index].draw()
        self.buttons[index + 1].selected = True
        self.buttons[index + 1].draw()

    def on_enter(self):
        index = self.get_selected_btn_index()
        self.buttons[index].on_enter()

    def show_settings(self):
        pass

    def start_game(self):
        self.clear()
        self.remove_events()
        game = Game(self.draw)
        game.start_game()
