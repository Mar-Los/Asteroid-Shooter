class Settings:
    buttons = []

    def draw(self):
        penup()
        setpos(Config.GAME_WIDTH / 2, Config.GAME_HEIGHT / 2)
        pendown()
        self.buttons.append(MenuButton('Hrát', start_game_fun, selected=True))
        self.buttons.append(MenuButton('Nastavení', self.show_settings))
        menu_start_y = (Config.GAME_HEIGHT - len(self.buttons) *
                        (Config.BUTTON_HEIGHT + Config.BUTTON_MARGIN) - Config.BUTTON_MARGIN) / 2
        for i in range(len(self.buttons)):
            self.buttons[i].start_pos = Config.GAME_WIDTH / 2 - Config.BUTTON_WIDTH / 2, menu_start_y + i * (
                Config.BUTTON_HEIGHT + Config.BUTTON_MARGIN) - Config.BUTTON_MARGIN
            self.buttons[i].draw()
        self.bind_events()

    def bind_events(self):
        onkey(self.on_enter, 'Return')
        onkey(self.select_upper_btn, 'Up')
        onkey(self.select_lower_btn, 'Down')
        listen()

    def remove_events(self):
        onkey(None, 'Return')
        onkey(None, 'Up')
        onkey(None, 'Down')

    def clear(self):
        for btn in self.buttons:
            btn.clear()