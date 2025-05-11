from tile import Tile


class Polyomino:
    def __init__(self, size, coord=None, tile_matrix=None, color="blue"):
        self.size = size
        self.coord = coord
        self.color = color

        if tile_matrix:
            self.tile_matrix = tile_matrix
        else:
            self.tile_matrix = self.gen_tile_matrix()

        if self.coord:
            self.tiles = self.get_tiles()

    def draw(self, surface):
        if not self.tiles:
            return
        for tile in self.tiles:
            tile.draw(surface)

    def set_coord(self, coord):
        self.coord = coord

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
        return tiles

    def gen_tile_matrix(self):
        num_tiles = self.size
        tiles = []
        tiles.append((0, 0))
        num_tiles -= 1
        while num_tiles > 0:
            for i in range(4):
                pass
