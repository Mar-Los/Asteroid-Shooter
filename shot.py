from turtle import Turtle, Vec2D
from config import Config
from asteroid import Asteroid
from math import sqrt


class Shot(Turtle):
    is_fired = False

    def __init__(self):
        super().__init__()
        self.speed(Config.SHOT_SPEED)
        self.pencolor(Config.SHOT_COLOR)

    def set_location(self, player_position: Vec2D, player_heading: Vec2D):
        self.penup()
        self.setpos(player_position)
        self.setheading(player_heading)
        self.start_position = self.pos()
        self.pendown()

    def intersection_with_asteroid(self, asteroid: Asteroid):
        shot_vector = self.start_position - self.pos()
        circle_shot_vector = asteroid.pos() - self.start_position

        a = shot_vector[0] ** 2 + shot_vector[1] ** 2
        b = 2 * (circle_shot_vector[0] * shot_vector[0] + circle_shot_vector[1] * shot_vector[1])
        c = circle_shot_vector[0] ** 2 + circle_shot_vector[1] ** 2 - asteroid.radius ** 2

        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return 'missed'

        result1 = (-b - sqrt(discriminant)) / (2 * a)
        result2 = (-b + sqrt(discriminant)) / (2 * a)
        if result1 >= 0 and result2 <= 1:
            return 'impaled'
        elif result1 >= 0 and result1 <= 1:
            return 'poked'
        else:
            return 'missed'
