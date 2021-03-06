from turtle import Turtle
from config import Config


class MenuButton(Turtle):
    startpos = ()
    def __init__(self, title: str, on_enter: callable, selected: bool = False):
        super().__init__(visible=False)
        self.pensize(0)
        self.speed(0)
        self.on_enter = on_enter
        self.title = title
        self.selected = selected
        self.penup()

    def draw(self):
        self.setpos(self.start_pos)
        if self.selected:
            self.fillcolor(Config.SELECTED_BUTTON_COLOR)
        else:
            self.fillcolor(Config.BUTTON_COLOR)
        self.pendown()
        self.begin_fill()
        for i in range(2):
            self.forward(Config.BUTTON_WIDTH)
            self.left(90)
            self.forward(Config.BUTTON_HEIGHT)
            self.left(90)
        self.end_fill()
        self.penup()
        self.forward(Config.BUTTON_WIDTH / 2)
        self.left(90)
        self.forward(3 / 2 * Config.FONT_SIZE + Config.BUTTON_HEIGHT / 2)
        self.color(Config.TEXT_COLOR)
        self.write(self.title, align='center',
                   font=(Config.FONT, Config.FONT_SIZE))
        self.penup()
        self.color(Config.BUTTON_COLOR)
        self.setheading(0)
        self.setpos(self.start_pos)