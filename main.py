import pygame

from constants import FPS_CAP, SCREEN_HEIGHT, SCREEN_WIDTH
from grid import Grid


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("0x1d2d44")
        playgrid = Grid()
        playgrid.update()
        playgrid.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS_CAP) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
