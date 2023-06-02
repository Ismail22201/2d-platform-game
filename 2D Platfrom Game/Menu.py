import pygame
import sys


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.width / 2, self.game.height / 2
        self.cursor_y = self.mid_h + 25

    def draw_cursor_1(self):
        self.game.draw_text_centre('>', 15, self.mid_w - 75, self.cursor_y, self.game.white)
        self.game.draw_text_centre('<', 15, self.mid_w + 75, self.cursor_y, self.game.white)

    def draw_cursor_2(self):
        self.game.draw_text_centre('>', 15, self.mid_w - 125, self.mid_h - 41, self.game.white)


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Play"
        self.play_h = self.mid_h + 25
        self.exit_h = self.mid_h + 50

    def display(self):
        self.check_input()
        self.game.draw_text_centre("Main Menu", 40, self.mid_w, self.mid_h - 100, self.game.white)
        self.game.draw_text_centre("Play", 20, self.mid_w, self.play_h, self.game.white)
        self.game.draw_text_centre("Exit", 20, self.mid_w, self.exit_h, self.game.white)
        self.draw_cursor_1()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Play":
                self.cursor_y = self.exit_h
                self.state = "Exit"
            elif self.state == "Exit":
                self.cursor_y = self.play_h
                self.state = "Play"

        if self.game.UP_KEY:
            if self.state == "Play":
                self.cursor_y = self.exit_h
                self.state = "Exit"
            elif self.state == "Exit":
                self.cursor_y = self.play_h
                self.state = "Play"

    def check_input(self):
        self.move_cursor()
        if self.game.ENTER_KEY:
            if self.state == "Play":
                self.game.playing = True
            if self.state == "Exit":
                pygame.quit()
                sys.exit()
