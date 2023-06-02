import pygame
import Spritesheet
from Player import Player


class Area:
    def __init__(self, game):
        self.game = game


class Area1(Area):
    def __init__(self, game):
        Area.__init__(self, game)
        self.background_image = pygame.image.load('Ground.png').convert_alpha()
        self.background = Spritesheet.SpriteSheet(self.background_image)
        self.player = Player(200, 275)

    def display(self):
        self.game.screen.blit(self.background.get_image(0, 1000, 1000, 0.5, (0, 0, 0)), (0, 0))
        self.player.move()
        self.player.render(self.game.screen)
