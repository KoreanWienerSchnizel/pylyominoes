import pygame
from pygame import Color, Rect

from constants import TILE_SIZE


class Tile:
    def __init__(self, coord, color="blue"):
        self.coord = coord
        self.color = Color(color)

    def draw(self, surface, tile_size=TILE_SIZE):
        if not self.coord:
            raise ValueError("Tile.draw: No Coord")
        tile_shadow_size = int(tile_size * 0.15)
        tile_dim = (tile_size, tile_size)
        grid_coord = (self.coord[0] * tile_size, self.coord[1] * tile_size)

        color = self.color.hsla
        light_value = color[2] * 1.3
        shade_value = color[2] * 0.7
        saturation = color[1] * 0.7
        light_color, dark_color = pygame.Color(0), pygame.Color(0)
        light_color.hsla = (color[0], saturation, light_value, color[3])
        dark_color.hsla = (color[0], saturation, shade_value, color[3])

        pygame.draw.rect(surface, self.color, Rect(grid_coord, tile_dim))
        # Top Highlight
        pygame.draw.rect(
            surface,
            light_color,
            Rect(
                grid_coord,
                (tile_size, tile_shadow_size),
            ),
        )
        # Bot Shadow
        pygame.draw.rect(
            surface,
            dark_color,
            Rect(
                (grid_coord[0], grid_coord[1] + (tile_size - tile_shadow_size)),
                (tile_size, tile_shadow_size),
            ),
        )
        # Left Highlight
        pygame.draw.rect(
            surface, light_color, Rect(grid_coord, (tile_shadow_size, tile_size))
        )
        # Right Shadow
        pygame.draw.rect(
            surface,
            dark_color,
            Rect(
                (grid_coord[0] + (tile_size - tile_shadow_size), grid_coord[1]),
                (tile_shadow_size, tile_size),
            ),
        )
