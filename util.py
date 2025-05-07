from constants import GRID_BUFFER_HEIGHT, TILE_SIZE


def get_playfield_coord(coord):
    return (coord[0] * TILE_SIZE, (coord[1] * TILE_SIZE) + GRID_BUFFER_HEIGHT)


def get_grid_coord(coord):
    return (coord[0] * TILE_SIZE, coord[1] * TILE_SIZE)
