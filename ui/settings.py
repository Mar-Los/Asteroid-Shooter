from turtle import numinput, listen
from math import floor
from app_config import AppConfig
from user_config import UserConfig
from .menu_button import MenuButton
from .menu import Menu


class Settings:
    def __init__(self, back_to_menu_fun: callable):
        self.back_to_menu_fun = back_to_menu_fun

    def draw(self):
        menu_center = (AppConfig.GAME_WIDTH / 2, AppConfig.GAME_HEIGHT / 2)
        self.menu = Menu(menu_center, self.get_buttons(), is_vertical=True, exit_on_enter=False, button_width=AppConfig.BUTTON_WIDTH * 2)
        self.menu.draw()

    def get_buttons(self):
        return [
            MenuButton('Dosah střel: ' + str(UserConfig.SHOT_REACH), self.change_shot_reach, selected=True, width=AppConfig.BUTTON_WIDTH * 2),
            MenuButton('Velikost hráče: ' + str(UserConfig.PLAYER_SIZE), self.change_player_size, width=AppConfig.BUTTON_WIDTH * 2),
            MenuButton('Rychlost hráče: ' + str(UserConfig.PLAYER_SPEED), self.change_player_speed, width=AppConfig.BUTTON_WIDTH * 2),
            MenuButton('Minimální velikost asteroidů: ' + str(UserConfig.ASTEROID_MIN_SIZE), self.change_asteroid_min_size, width=AppConfig.BUTTON_WIDTH * 2),
            MenuButton('Maximální velikost asteroidů: ' + str(UserConfig.ASTEROID_MAX_SIZE), self.change_asteroid_max_size, width=AppConfig.BUTTON_WIDTH * 2),
            MenuButton('Minimální počet asteroidů: ' + str(UserConfig.MIN_ASTEROIDS), self.change_min_asteroids, width=AppConfig.BUTTON_WIDTH * 2),
            MenuButton('Maximální velikost asteroidů: ' + str(UserConfig.MAX_ASTEROIDS), self.change_max_asteroids, width=AppConfig.BUTTON_WIDTH * 2),
            MenuButton('Zpět do menu', self.back_to_menu, width=AppConfig.BUTTON_WIDTH * 2)
        ]

    def back_to_menu(self):
        self.menu.clear()
        self.back_to_menu_fun()

    def update_menu(self):
        self.menu.clear()
        self.menu.buttons = self.get_buttons()
        self.menu.draw()
        self.menu.bind_events()

    def change_user_setting(self, setting_name: str, title: str, prompt: str, min_value: int, max_value: int):
        try:
            newValue = floor(numinput(
                title, prompt, int((min_value + max_value) / 2), min_value, max_value
            ))
            setattr(UserConfig, setting_name, newValue)
            self.update_menu()
        except:
            pass

    def change_shot_reach(self):
        self.change_user_setting('SHOT_REACH', 'Dosah střel', 'Zadej dosah střel', 100, 1000)

    def change_player_size(self):
        self.change_user_setting('PLAYER_SIZE', 'Velikost hráče', 'Zadej velikost hráče', 5, 20)
    
    def change_player_speed(self):
        self.change_user_setting('PLAYER_SPEED', 'Rychlost hráče', 'Zadej rychlost hráče', 1, 7)

    def change_asteroid_min_size(self):
        self.change_user_setting('ASTEROID_MIN_SIZE', 'Minimální velikost asteroidů', 'Zadej minimální velikost asteroidů', 5, 80)

    def change_asteroid_max_size(self):
        self.change_user_setting('ASTEROID_MAX_SIZE', 'Maximální velikost asteroidů', 'Zadej maximální velikost asteroidů', 85, 200)

    def change_min_asteroids(self):
        self.change_user_setting('MIN_ASTEROIDS', 'Minimum asteroidů', 'Zadej minimum asteroidů', 1, 10)

    def change_max_asteroids(self):
        self.change_user_setting('MAX_ASTEROIDS', 'Maximum asteroidů', 'Zadej maximum asteroidů', 10, 30)
