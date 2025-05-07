import pygame

from constants import TILE_SIZE
from util import get_grid_coord


class Tile:
    def __init__(self, coord):
        self.coord = coord
        self.tile = pygame.Rect(get_grid_coord(self.coord), (TILE_SIZE, TILE_SIZE))


class Polyomino:
    def __init__(self, size, coord, tile_matrix=None, color="blue"):
        self.size = size
        self.coord = coord
        self.color = color

        if tile_matrix:
            self.tile_matrix = tile_matrix
        else:
            self.tile_matrix = self.gen_tile_matrix()

        self.tiles = self.get_tiles()

    def get_tiles(self):
        tiles = []
        m_height = len(self.tile_matrix)
        m_width = len(self.tile_matrix[0])
        for y in range(m_height):
            for x in range(m_width):
                if self.tile_matrix[y][x] == 1:
                    pass

    def gen_tile_matrix(self):
        num_tiles = self.size
        tiles = []
        tiles.append((0, 0))
        num_tiles -= 1
        while num_tiles > 0:
            for i in range(4):
                pass
