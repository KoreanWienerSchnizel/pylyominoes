import pygame
from pygame.color import Color

from constants import FPS_CAP, SCREEN_HEIGHT, SCREEN_WIDTH
from grid import Grid


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        dt = 0
        background_color = Color("0x1d2d44")
        game_grid = Grid()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.screen.fill(background_color)
            game_grid.update()
            game_grid.draw(self.screen)

            pygame.display.flip()
            dt = self.clock.tick(FPS_CAP)
            print(dt)
