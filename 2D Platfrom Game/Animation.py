import pygame
import Spritesheet


class Animation:
    def __init__(self, game):
        self.game = game
        self.animation_list = []
        self.animation_steps = []
        self.action = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = []
        self.frame = 0
        self.step_counter = 0


class PlayerCore(Animation):
    def __init__(self, game):
        Animation.__init__(self, game)
        self.sprite_sheet_image = pygame.image.load('Green Cubic Core.png').convert_alpha()
        self.sprite_sheet = Spritesheet.SpriteSheet(self.sprite_sheet_image)
        self.animation_steps = [2]
        self.animation_cooldown = [100, 900]
        self.x, self.y = 0, 0

        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, 100, 100, 1, (0, 0, 0)))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)

    def display(self, screen, pos):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown[self.frame]:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0

        screen.blit(self.animation_list[self.action][self.frame], pos)
