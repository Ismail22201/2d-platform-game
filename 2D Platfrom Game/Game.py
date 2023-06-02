from pygame.locals import *
from Area import Area1
from Menu import *
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.ENTER_KEY, self.BACK_KEY = False, False
        self.DOWN_KEY, self.UP_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False
        self.width, self.height, self.fps = 500, 500, 60
        self.clock = pygame.time.Clock()
        self.font_name = "Font/upheavtt.ttf"
        self.black, self.white = (0, 0, 0), (255, 255, 255)
        self.screen = pygame.Surface((self.width, self.height))
        self.window = pygame.display.set_mode((self.width, self.height))
        self.main_menu = MainMenu(self)
        self.curr_display = MainMenu(self)
        self.curr_area = Area1(self)

    def loop(self):
        while self.running:
            self.clock.tick(self.fps)
            self.check_events()
            self.screen.fill(self.black)
            if not self.playing:
                self.curr_display.display()
            else:
                self.curr_area.display()
            self.window.blit(self.screen, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True

    def reset_keys(self):
        self.ENTER_KEY, self.BACK_KEY = False, False
        self.DOWN_KEY, self.UP_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False

    def draw_text_centre(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_text_left(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.screen.blit(text_surface, text_rect)
