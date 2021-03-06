from turtle import Turtle, onkey
from app_config import AppConfig

class EndScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.color(AppConfig.TEXT_COLOR)

    def draw(self, game_result: bool):
        self.penup()
        self.setpos(AppConfig.GAME_WIDTH / 2, AppConfig.GAME_HEIGHT / 2)
        if game_result:
            self.write('Vyhrál jsi!', align='center', font=(
                AppConfig.FONT, AppConfig.FONT_SIZE * 2))
        else:
            self.write('Prohrál jsi!', align='center', font=(
                AppConfig.FONT, AppConfig.FONT_SIZE * 2))
        self.penup()
        self.setpos(AppConfig.GAME_WIDTH / 2, AppConfig.GAME_HEIGHT /
               2 + AppConfig.FONT_SIZE * 2 + 10)
        self.pendown()
        self.write('Pro novou hru stiskni enter', align='center',
              font=(AppConfig.FONT, AppConfig.FONT_SIZE))