from turtle import Turtle
from random import randint
from app_config import AppConfig
from user_config import UserConfig


class Asteroid(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(0)
        self.fillcolor(AppConfig.ASTEROID_COLOR)
        self.color(AppConfig.ASTEROID_COLOR)
        self.speed(0)
        self.hideturtle()
        self.radius = randint(UserConfig.ASTEROID_MIN_SIZE,
                              UserConfig.ASTEROID_MAX_SIZE)

    def set_location(self):
        x_in_center, y_in_center = True, True
        while x_in_center and y_in_center:
            self.setpos(AppConfig.GAME_WIDTH - randint(self.radius, AppConfig.GAME_WIDTH),
                        AppConfig.GAME_HEIGHT - randint(self.radius, AppConfig.GAME_HEIGHT))
            x_in_center = self.xcor() >= (AppConfig.GAME_WIDTH - AppConfig.CENTER_AREA_WIDTH) / \
                2 and self.xcor() <= (AppConfig.GAME_WIDTH + AppConfig.CENTER_AREA_WIDTH) / 2
            y_in_center = self.ycor() >= (AppConfig.GAME_HEIGHT - AppConfig.CENTER_AREA_HEIGHT) / \
                2 and self.ycor() <= (AppConfig.GAME_HEIGHT + AppConfig.CENTER_AREA_HEIGHT) / 2

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
