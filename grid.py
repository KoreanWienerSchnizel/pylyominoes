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
        self.col = GRID_COL
        self.row = GRID_ROW
        self.grid_matrix = [[0 for _ in range(self.col)] for _ in range(self.row)]
        self.grid_surface = pygame.surface.Surface((GRID_WIDTH, GRID_HEIGHT))

    def draw(self, screen):
        screen.blit(self.grid_surface, (GRID_OFFSET_X, GRID_OFFSET_Y))

    def update(self):
        self.grid_surface.fill("0x3e5c76")
        self.draw_grid()
        self.draw_gridlines()

    def place_piece(self, piece):
        if not piece.coord:
            raise ValueError("Grid.place_piece: no coord given")

        for y in range(len(piece.tile_matrix)):
            for x in range(len(piece.tile_matrix[y])):
                self.grid_matrix[piece.coord[1] + y][piece.coord[0] + x] = (
                    piece.tile_matrix[y][x]
                )

    def check_open_space(self, coord):
        if coord[0] < 0 or coord[0] >= self.col:
            return False
        if coord[1] >= self.row:
            return False
        return self.grid_matrix[coord[1]][coord[0]] == 0

    def draw_grid(self):
        for y in range(len(self.grid_matrix)):
            for x in range(len(self.grid_matrix[y])):
                if self.grid_matrix[y][x] == 1:
                    Tile((x, y), "#989898").draw(self.grid_surface)

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
