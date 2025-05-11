import pygame
from pygame.color import Color
from pygame.rect import Rect

from constants import TILE_DIM, TILE_SHADOW_SIZE, TILE_SIZE
from util import get_grid_coord


class Tile:
    def __init__(self, coord, color="blue"):
        self.coord = coord
        self.color = Color(color)

    def draw(self, surface):
        if not self.coord:
            raise ValueError("Tile draw func: No Coord")
        color = self.color.hsla
        light_value = color[2] * 1.3
        shade_value = color[2] * 0.7
        saturation = color[1] * 0.7
        light_color, dark_color = pygame.Color(0), pygame.Color(0)
        light_color.hsla = (color[0], saturation, light_value, color[3])
        dark_color.hsla = (color[0], saturation, shade_value, color[3])
        grid_coord = get_grid_coord(self.coord)
        pygame.draw.rect(surface, self.color, Rect(grid_coord, TILE_DIM))
        # Top Highlight
        pygame.draw.rect(
            surface,
            light_color,
            Rect(
                grid_coord,
                (TILE_SIZE, TILE_SHADOW_SIZE),
            ),
        )
        # Bot Shadow
        pygame.draw.rect(
            surface,
            dark_color,
            Rect(
                (grid_coord[0], grid_coord[1] + (TILE_SIZE - TILE_SHADOW_SIZE)),
                (TILE_SIZE, TILE_SHADOW_SIZE),
            ),
        )
        # Left Highlight
        pygame.draw.rect(
            surface, light_color, Rect(grid_coord, (TILE_SHADOW_SIZE, TILE_SIZE))
        )
        # Right Shadow
        pygame.draw.rect(
            surface,
            dark_color,
            Rect(
                (grid_coord[0] + (TILE_SIZE - TILE_SHADOW_SIZE), grid_coord[1]),
                (TILE_SHADOW_SIZE, TILE_SIZE),
            ),
        )


class Polyomino:
    def __init__(self, size, coord, tile_matrix=None, color="blue"):
        self.size = size
        self.coord = coord
        self.color = color

        if tile_matrix:
            self.tile_matrix = tile_matrix
        else:
            self.tile_matrix = self.gen_tile_matrix()

        if self.coord:
            self.tiles = self.get_tiles()

    def get_tiles(self):
        tiles = []
        m_height = len(self.tile_matrix)
        m_width = len(self.tile_matrix[0])
        for y in range(m_height):
            for x in range(m_width):
                if self.tile_matrix[y][x] == 1:
                    tiles.append(
                        Tile((self.coord[0] + x, self.coord[1] + y), self.color)
                    )

    def gen_tile_matrix(self):
        num_tiles = self.size
        tiles = []
        tiles.append((0, 0))
        num_tiles -= 1
        while num_tiles > 0:
            for i in range(4):
                pass
