from turtle import Turtle
from app_config import AppConfig


class MenuButton(Turtle):
    startpos = ()
    def __init__(self, title: str, on_enter: callable, selected: bool = False, width: int = AppConfig.BUTTON_WIDTH):
        super().__init__(visible=False)
        self.pensize(0)
        self.speed(0)
        self.on_enter = on_enter
        self.title = title
        self.selected = selected
        self.width = width
        self.penup()

    def draw(self):
        self.setpos(self.start_pos)
        if self.selected:
            self.fillcolor(AppConfig.SELECTED_BUTTON_COLOR)
        else:
            self.fillcolor(AppConfig.BUTTON_COLOR)
        self.pendown()
        self.begin_fill()
        for i in range(2):
            self.forward(self.width)
            self.left(90)
            self.forward(AppConfig.BUTTON_HEIGHT)
            self.left(90)
        self.end_fill()
        self.penup()
        self.forward(self.width / 2)
        self.left(90)
        self.forward(3 / 2 * AppConfig.FONT_SIZE + AppConfig.BUTTON_HEIGHT / 2)
        self.color(AppConfig.TEXT_COLOR)
        self.write(self.title, align='center',
                   font=(AppConfig.FONT, AppConfig.FONT_SIZE))
        self.penup()
        self.color(AppConfig.BUTTON_COLOR)
        self.setheading(0)
        self.setpos(self.start_pos)