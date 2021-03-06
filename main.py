from ui.menu import Menu
from app_config import AppConfig
from turtle import *


def setup_window():
    setup(width=AppConfig.GAME_WIDTH, height=AppConfig.GAME_HEIGHT)
    setworldcoordinates(0, AppConfig.GAME_HEIGHT, AppConfig.GAME_WIDTH, 0)
    bgcolor(AppConfig.BACKGROUND_COLOR)
    title('Asteroid Shooter')

def main():
    setup_window()
    menu = Menu()
    menu.draw()


if __name__ == '__main__':
    main()
