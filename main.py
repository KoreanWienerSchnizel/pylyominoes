import pygame
from pygame.color import Color

from constants import FPS_CAP, SCREEN_HEIGHT, SCREEN_WIDTH
from grid import Grid


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    background_color = Color("0x1d2d44")
    color = background_color
    lerp_value = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(color)
        color = background_color.lerp(Color("black"), lerp_value)
        lerp_value += 0.1
        if lerp_value >= 1:
            lerp_value = 0
        print(lerp_value)
        playgrid = Grid()
        playgrid.update()
        playgrid.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS_CAP) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
