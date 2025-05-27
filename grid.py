import pygame
from pygame.rect import Rect

from constants import (
    GRID_BUFFER_HEIGHT,
    GRID_BUFFER_ROW,
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
        m_length = len(piece.tile_matrix)
        for y in range(m_length):
            for x in range(m_length):
                if piece.tile_matrix[y][x] == 1:
                    self.grid_matrix[piece.coord[1] + y][piece.coord[0] + x] = 1
        return self.check_grid()

    def check_grid(self):
        lines_cleared = 0
        lines_to_clear = []
        for y in range(GRID_BUFFER_ROW, self.row):
            if all(self.grid_matrix[y]):
                lines_cleared += 1
                lines_to_clear.append(y)
        for line in lines_to_clear:
            self.clear_line(line)

        for y in range(GRID_BUFFER_ROW):
            if any(self.grid_matrix[y]):
                print(y)
                return -1
        return lines_cleared

    def clear_line(self, line_num):
        clear_line = [0 for _ in range(self.col)]
        self.grid_matrix.pop(line_num)
        self.grid_matrix.insert(0, clear_line)

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
