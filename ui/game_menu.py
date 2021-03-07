from turtle import bye
from app_config import AppConfig
from .menu_button import MenuButton
from .settings import Settings
from game.main import Game
from .menu import Menu


class GameMenu:

    def draw(self):
        buttons = [
            MenuButton('Hrát', self.start_game, selected=True),
            MenuButton('Nastavení', self.show_settings),
            MenuButton('Konec', self.quit_game)
        ]
        menu_center = (AppConfig.GAME_WIDTH / 2, AppConfig.GAME_HEIGHT / 2)
        menu = Menu(menu_center, buttons, is_vertical=True)
        menu.draw()

    def show_settings(self):
        settings = Settings(self.draw)
        settings.draw()

    def start_game(self):
        game = Game(self.draw)
        game.start_game()

    def quit_game(self):
        bye()