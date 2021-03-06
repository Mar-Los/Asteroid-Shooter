from turtle import Turtle
from math import sqrt, sin, cos, pi
from app_config import AppConfig
from user_config import UserConfig
from .asteroid import Asteroid

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color(AppConfig.PLAYER_COLOR)
        self.turtlesize(UserConfig.PLAYER_SIZE)
        self.speed(0)
        self.penup()
        self.setpos(AppConfig.GAME_WIDTH / 2, AppConfig.GAME_HEIGHT / 2)

    def move_forward(self):
        self.forward(AppConfig.PLAYER_ACCELERATION_SPEED)

    def move_left(self):
        self.right(10)

    def move_right(self):
        self.left(10)

    def intersects_with_asteroid(self, asteroid: Asteroid):
        hitbox_radius = UserConfig.PLAYER_SIZE * AppConfig.PLAYER_SIZE_TO_HITBOX_RADIUS_RATIO
        hitbox_centre_x_coor = self.xcor() - hitbox_radius * cos((pi * self.heading()) / 180)
        hitbox_centre_y_coor = self.ycor() - hitbox_radius * sin((pi * self.heading()) / 180)
        distance_from_centres = sqrt((hitbox_centre_x_coor - asteroid.xcor()) ** 2 + (hitbox_centre_y_coor - asteroid.ycor()) ** 2)
        if distance_from_centres > hitbox_radius + asteroid.radius:
            return False
        else:
            return True
