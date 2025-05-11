import pygame
from pygame.rect import Rect

from constants import (
    GRID_BUFFER_HEIGHT,
    GRID_COL,
    GRID_HEIGHT,
    GRID_OFFSET_X,
    GRID_OFFSET_Y,
    GRID_PLAYFIELD_HEIGHT,
    GRID_PLAYFIELD_ROW,
    GRID_ROW,
    GRID_WIDTH,
)
from polyomino import Tile
from util import get_playfield_coord


class Grid:
    def __init__(self):
        self.grid_matrix = [[0 for _ in range(GRID_COL)] for _ in range(GRID_ROW)]
        self.grid_surface = pygame.surface.Surface((GRID_WIDTH, GRID_HEIGHT))
        self.live_piece = None

    def draw(self, screen):
        screen.blit(self.grid_surface, (GRID_OFFSET_X, GRID_OFFSET_Y))

    def update(self):
        self.grid_surface.fill("0x3e5c76")
        tile0 = Tile((0, GRID_ROW - 1))
        tile1 = Tile((0, 10), "green")
        tile0.draw(self.grid_surface)
        tile1.draw(self.grid_surface)
        self.draw_gridlines()

    def draw_gridlines(self):
        for x in range(GRID_COL):
            pygame.draw.line(
                self.grid_surface,
                "black",
                get_playfield_coord((x, 0)),
                get_playfield_coord((x, GRID_PLAYFIELD_ROW)),
            )
        for y in range(GRID_PLAYFIELD_ROW):
            pygame.draw.line(
                self.grid_surface,
                "black",
                get_playfield_coord((0, y)),
                get_playfield_coord((GRID_COL, y)),
            )
        pygame.draw.rect(
            self.grid_surface,
            "white",
            Rect((0, GRID_BUFFER_HEIGHT), (GRID_WIDTH, GRID_PLAYFIELD_HEIGHT)),
            width=1,
        )
