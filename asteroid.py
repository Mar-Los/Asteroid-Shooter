from turtle import Turtle
from config import Config
from random import randint


class Asteroid(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(0)
        self.fillcolor(Config.ASTEROID_COLOR)
        self.color(Config.ASTEROID_COLOR)
        self.speed(0)
        self.hideturtle()
        self.radius = randint(Config.ASTEROID_MIN_SIZE,
                              Config.ASTEROID_MAX_SIZE)

    def set_location(self):
        x_in_center, y_in_center = True, True
        while x_in_center and y_in_center:
            self.setpos(Config.GAME_WIDTH - randint(self.radius, Config.GAME_WIDTH),
                        Config.GAME_HEIGHT - randint(self.radius, Config.GAME_HEIGHT))
            x_in_center = self.xcor() >= (Config.GAME_WIDTH - Config.CENTER_AREA_WIDTH) / \
                2 and self.xcor() <= (Config.GAME_WIDTH + Config.CENTER_AREA_WIDTH) / 2
            y_in_center = self.ycor() >= (Config.GAME_HEIGHT - Config.CENTER_AREA_HEIGHT) / \
                2 and self.ycor() <= (Config.GAME_HEIGHT + Config.CENTER_AREA_HEIGHT) / 2

    def draw(self):
        self.penup()
        self.set_location()
        self.setpos(self.xcor(), self.ycor() - self.radius)
        self.pendown()
        self.begin_fill()
        self.circle(self.radius)
        self.end_fill()
        self.penup()
        self.setpos(self.xcor(), self.ycor() + self.radius)
