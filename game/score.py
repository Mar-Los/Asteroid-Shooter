from turtle import Turtle
from app_config import AppConfig

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color(AppConfig.SCORE_COLOR)
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.setpos(AppConfig.GAME_WIDTH - 10, 2 * AppConfig.FONT_SIZE + 5)
        self.pendown()

    def update(self, score: int):
        self.clear()
        self.write('Skóre: ' + '{:05}'.format(score), align='right', font=(AppConfig.FONT, AppConfig.FONT_SIZE))
