from menu import Menu
from config import Config
from turtle import *


def setup_window():
    setup(width=Config.GAME_WIDTH, height=Config.GAME_HEIGHT)
    setworldcoordinates(0, Config.GAME_HEIGHT, Config.GAME_WIDTH, 0)
    bgcolor(Config.BACKGROUND_COLOR)
    title('Asteroid Shooter')

def main():
    setup_window()
    menu = Menu()
    menu.draw()


if __name__ == '__main__':
    main()
