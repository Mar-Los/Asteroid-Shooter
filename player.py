from turtle import Turtle
from config import Config
from asteroid import Asteroid
from math import sqrt, sin, cos, pi

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color(Config.PLAYER_COLOR)
        self.turtlesize(Config.PLAYER_SIZE)
        self.speed(0)
        self.penup()
        self.setpos(Config.GAME_WIDTH / 2, Config.GAME_HEIGHT / 2)

    def move_forward(self):
        self.forward(Config.PLAYER_ACCELERATION_SPEED)

    def move_left(self):
        self.right(10)

    def move_right(self):
        self.left(10)

    def intersects_with_asteroid(self, asteroid: Asteroid):
        hitbox_radius = Config.PLAYER_SIZE * Config.PLAYER_SIZE_TO_HITBOX_RADIUS_RATIO
        hitbox_centre_x_coor = self.xcor() - hitbox_radius * cos((pi * self.heading()) / 180)
        hitbox_centre_y_coor = self.ycor() - hitbox_radius * sin((pi * self.heading()) / 180)
        distance_from_centres = sqrt((hitbox_centre_x_coor - asteroid.xcor()) ** 2 + (hitbox_centre_y_coor - asteroid.ycor()) ** 2)
        if distance_from_centres > hitbox_radius + asteroid.radius:
            return False
        else:
            return True
