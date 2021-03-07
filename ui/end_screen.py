from turtle import Turtle, onkey
from app_config import AppConfig
from .menu import Menu

class EndScreen(Turtle):
    def __init__(self, score: int, buttons: list):
        super().__init__()
        self.score = score
        self.buttons = buttons
        self.hideturtle()
        self.speed(0)
        self.color(AppConfig.TEXT_COLOR)

    def draw(self):
        self.penup()
        self.setpos(AppConfig.GAME_WIDTH / 2, AppConfig.GAME_HEIGHT / 2)
        font = (AppConfig.FONT, AppConfig.FONT_SIZE * 2)
        self.write('Scóre: ' + str(self.score), align='center', font=font)
        menu_center = (AppConfig.GAME_WIDTH / 2, AppConfig.GAME_HEIGHT /
               2 + AppConfig.FONT_SIZE * 2 + AppConfig.BUTTON_MARGIN)
        end_menu = Menu(menu_center, self.buttons, is_vertical=False)
        end_menu.draw()
