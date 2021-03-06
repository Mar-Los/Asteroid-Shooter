from turtle import *
from menu import Menu
from score import Score
from config import Config
from player import Player
from shot import Shot
from asteroid import Asteroid
from math import floor


class Game:
    shots = []
    asteroids = []
    score = 0

    def __init__(self):
        setup(width=Config.GAME_WIDTH, height=Config.GAME_HEIGHT)
        setworldcoordinates(0, Config.GAME_HEIGHT, Config.GAME_WIDTH, 0)
        bgcolor(Config.BACKGROUND_COLOR)
        title('Spaceship Battle')
        hideturtle()
        speed(0)
        color(Config.PLAYER_COLOR)
        self.menu = Menu()
        self.score_bar = Score()

    def startup(self):
        clear()
        self.menu.draw(self.start_game)
        done()

    def start_game(self):
        clear()
        self.menu.remove_events()
        self.menu.clear()
        try:
            asteroid_count = floor(numinput(
                'Počet asteroidů', 'Zadej počet asteroidů',
                minval=Config.MIN_ASTEROIDS,
                maxval=Config.MAX_ASTEROIDS,
                default=floor((Config.MIN_ASTEROIDS + Config.MAX_ASTEROIDS) / 2)
            ))
        except TypeError:
            asteroid_count = floor((Config.MIN_ASTEROIDS + Config.MAX_ASTEROIDS) / 2)
        self.draw_asteroids(asteroid_count)
        self.player = Player()
        self.bind_events()
        self.score_bar.update(self.score)
        while(True):
            if not self.asteroids:
                self.end(won=True)
                return
            for asteroid in self.asteroids:
                if self.player.intersects_with_asteroid(asteroid):
                    self.end(won=False)
                    return
            self.move_player()
            self.move_shots()

    def move_player(self):
        playerRadius = Config.PLAYER_SIZE * Config.PLAYER_SIZE_TO_HITBOX_RADIUS_RATIO
        if self.player.xcor() - playerRadius > Config.GAME_WIDTH:
            self.player.setpos(0, self.player.ycor())
        elif self.player.xcor() + playerRadius < 0:
            self.player.setpos(Config.GAME_WIDTH, self.player.ycor())
        elif self.player.ycor() - playerRadius > Config.GAME_HEIGHT:
            self.player.setpos(self.player.xcor(), 0)
        elif self.player.ycor() + playerRadius < 0:
            self.player.setpos(self.player.xcor(), Config.GAME_HEIGHT)
        self.player.forward(Config.PLAYER_SPEED)

    def move_shots(self):
        for shot in self.shots:
            if not shot.is_fired:
                shot.forward(Config.SHOT_REACH)
                shot.is_fired = True
                for asteroid in self.asteroids:
                    intersection = shot.intersection_with_asteroid(asteroid)
                    if intersection == 'missed':
                        continue
                    asteroid.clear()
                    self.asteroids.remove(asteroid)
                    if intersection == 'impaled':
                        self.score += round(Config.IMPALE_SCORE * (1 /
                                                                   asteroid.radius) * Config.ASTEROID_SIZE_SCORE_RATIO)
                    elif intersection == 'poked':
                        self.score += round(Config.POKE_SCORE * (1 / asteroid.radius)
                                            * Config.ASTEROID_SIZE_SCORE_RATIO)
                    self.score_bar.update(self.score)
                    del asteroid

            else:
                shot.clear()
                self.shots.remove(shot)
                shot.hideturtle()
                del shot

    def bind_events(self):
        onkeypress(self.player.move_forward, 'Up')
        onkeypress(self.player.move_left, 'Left')
        onkeypress(self.player.move_right, 'Right')
        onkey(self.fire_shot, 'space')
        listen()

    def remove_events(self):
        onkeypress(None, 'Up')
        onkeypress(None, 'Left')
        onkeypress(None, 'Right')
        onkey(None, 'space')

    def fire_shot(self):
        shot = Shot()
        shot.set_location(self.player.pos(), self.player.heading())
        self.shots.append(shot)

    def draw_asteroids(self, asteroid_count):
        for i in range(asteroid_count):
            self.asteroids.append(Asteroid())
            self.asteroids[i].draw()

    def reset(self):
        for asteroid in self.asteroids:
            asteroid.clear()
        for shot in self.shots:
            shot.clear()
            shot.hideturtle()
        self.asteroids.clear()
        self.player.clear()
        self.player.hideturtle()

    def end(self, won: bool):
        self.remove_events()
        penup()
        setpos(Config.GAME_WIDTH / 2, Config.GAME_HEIGHT / 2)
        self.reset()
        if won:
            write('Vyhrál jsi!', align='center', font=(
                Config.FONT, Config.FONT_SIZE * 2))
        else:
            write('Prohrál jsi!', align='center', font=(
                Config.FONT, Config.FONT_SIZE * 2))
            self.score = 0
        penup()
        setpos(Config.GAME_WIDTH / 2, Config.GAME_HEIGHT /
               2 + Config.FONT_SIZE * 2 + 10)
        pendown()
        write('Pro novou hru stiskni enter', align='center',
              font=(Config.FONT, Config.FONT_SIZE))
        onkey(self.start_game, 'Return')
