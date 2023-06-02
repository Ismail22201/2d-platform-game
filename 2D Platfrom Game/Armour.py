import pygame
import Spritesheet


class Armour:
    def __init__(self, game):
        self.game = game


class Armour1(Armour):
    def __init__(self, game):
        Armour.__init__(self, game)
        self.armour1_image = pygame.image.load('Cubic Armour.png').convert_alpha()
        self.armour1 = Spritesheet.SpriteSheet(self.armour1_image)

    def display(self, screen, pos):
        screen.blit(self.armour1.get_image(0, 108, 108, 1, (0, 0, 0)), pos)
