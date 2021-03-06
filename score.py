from turtle import Turtle
from config import Config

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color(Config.SCORE_COLOR)
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.setpos(Config.GAME_WIDTH - 10, 2 * Config.FONT_SIZE + 5)
        self.pendown()

    def update(self, score: int):
        self.clear()
        self.write('Skóre: ' + '{:05}'.format(score), align='right', font=(Config.FONT, Config.FONT_SIZE))
