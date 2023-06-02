import pygame
from Animation import PlayerCore
from pygame.locals import *

from Armour import Armour1

vec = pygame.math.Vector2


class Player:
    def __init__(self, x, y):
        self.animation = PlayerCore(self)
        self.armour = Armour1(self)
        self.pos = vec(x, y)
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)
        self.ACC = 0.4
        self.FRIC = -0.1

    def move(self):

        self.acc = vec(0, 0)

        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.acc.x = -self.ACC
        if keys[K_RIGHT]:
            self.acc.x = self.ACC

        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

    def render(self, screen):
        self.animation.display(screen, self.pos)
        self.armour.display(screen, self.pos - vec(4, 4))
