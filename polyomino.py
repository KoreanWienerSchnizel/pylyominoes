from constants import PREVIEW_SIZE, Move
from tile import Tile


class Polyomino:
    def __init__(self, size, tile_matrix, coord=None, color="blue"):
        self.size = size
        self.tile_matrix = tile_matrix
        self.coord = coord
        self.color = color
        self.tiles = []

        if self.coord:
            self.tiles = self.get_tiles()

    def draw(self, surface):
        if not self.tiles:
            return
        for tile in self.tiles:
            tile.draw(surface)

    def draw_preview(self, surface):
        if not self.tile_matrix:
            return
        m_len = len(self.tile_matrix)
        tile_size = PREVIEW_SIZE // m_len
        for y in range(m_len):
            for x in range(m_len):
                if self.tile_matrix[y][x] == 1:
                    Tile((x, y), self.color).draw(surface, tile_size)

    def move(self, direction, grid):
        match direction:
            case Move.UP:
                for tile in self.tiles:
                    new_coord = (self.coord[0], self.coord[1] - 1)
                    if not grid.check_open_space(new_coord):
                        return False
                for tile in self.tiles:
                    tile.coord = (tile.coord[0], tile.coord[1] - 1)
                self.coord = new_coord

            case Move.DOWN:
                for tile in self.tiles:
                    new_coord = (tile.coord[0], tile.coord[1] + 1)
                    if not grid.check_open_space(new_coord):
                        return False
                for tile in self.tiles:
                    tile.coord = (tile.coord[0], tile.coord[1] + 1)
                self.coord = (self.coord[0], self.coord[1] + 1)

            case Move.LEFT:
                for tile in self.tiles:
                    new_coord = (tile.coord[0] - 1, tile.coord[1])
                    if not grid.check_open_space(new_coord):
                        return False
                for tile in self.tiles:
                    tile.coord = (tile.coord[0] - 1, tile.coord[1])
                self.coord = (self.coord[0] - 1, self.coord[1])

            case Move.RIGHT:
                for tile in self.tiles:
                    new_coord = (tile.coord[0] + 1, tile.coord[1])
                    if not grid.check_open_space(new_coord):
                        return False
                for tile in self.tiles:
                    tile.coord = (tile.coord[0] + 1, tile.coord[1])
                self.coord = (self.coord[0] + 1, self.coord[1])

            case _:
                raise ValueError("Polyomino.move: Incorrect/No direction specified")
        return True

    def rotate(self, grid):
        new_tile_matrix = []
        tmp_arr = []
        m_length = len(self.tile_matrix)
        for x in range(m_length):
            for y in range(m_length - 1, -1, -1):
                tmp_arr.append(self.tile_matrix[y][x])
            new_tile_matrix.append(tmp_arr)
            tmp_arr = []

        new_coord = self.wallkick_test(new_tile_matrix, grid)
        if new_coord is None:
            return False
        self.coord = new_coord
        self.tile_matrix = new_tile_matrix
        self.tiles = self.get_tiles()
        return True

    def wallkick_test(self, new_tile_matrix, grid):
        m_length = len(self.tile_matrix)
        test_coords = [(self.coord[0], self.coord[1])]
        for i in range(1, (m_length // 2) + 1):
            for j in range(1, (m_length // 2) + 1):
                test_coords.append((self.coord[0] - j, self.coord[1]))
                test_coords.append((self.coord[0] + j, self.coord[1]))
                test_coords.append((self.coord[0], self.coord[1] + i))
                test_coords.append((self.coord[0], self.coord[1] - i))
                test_coords.append((self.coord[0] - j, self.coord[1] - i))
                test_coords.append((self.coord[0] + j, self.coord[1] - i))
                test_coords.append((self.coord[0] - j, self.coord[1] + i))
                test_coords.append((self.coord[0] + j, self.coord[1] + i))

        for coord in test_coords:
            if self.check_new_tile_matrix_coord(coord, new_tile_matrix, grid):
                return coord
        return None

    def check_new_tile_matrix_coord(self, new_coord, tile_matrix, grid):
        m_len = len(tile_matrix)
        for y in range(m_len):
            for x in range(m_len):
                if tile_matrix[y][x] == 1:
                    if not grid.check_open_space((new_coord[0] + x, new_coord[1] + y)):
                        return False
        return True

    def get_tiles(self):
        tiles = []
        m_length = len(self.tile_matrix)
        for y in range(m_length):
            for x in range(m_length):
                if self.tile_matrix[y][x] == 1:
                    tiles.append(
                        Tile((self.coord[0] + x, self.coord[1] + y), self.color)
                    )
        return tiles

    def gen_tile_matrix(self):
        raise Exception("Polyomino.gen_tile_matrix: not implemented yet")
        num_tiles = self.size
        tiles = []
        tiles.append((0, 0))
        num_tiles -= 1
        while num_tiles > 0:
            for i in range(4):
                pass
