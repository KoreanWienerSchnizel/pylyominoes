import random

from polyomino import Polyomino
from util import gen_random_color


class Bag:
    def __init__(self, tile_matrix_list=None):
        self.polyomino_set = []
        self.bag = []
        if tile_matrix_list:
            self.populate_set(tile_matrix_list)
            self.populate_bag()

    def populate_set(self, tile_matrix_list, color_list=None):
        if not tile_matrix_list:
            raise Exception("Bag.populate_set: No Tile Matrix found")
        for matrix in tile_matrix_list:
            size = sum([sum(i) for i in matrix])
            if len(color_list) > 0:
                color = color_list.pop(0)
            else:
                color = gen_random_color()
            self.add_polyomino_set(matrix, size, color)

    def add_polyomino_set(self, matrix, size, color):
        self.polyomino_set.append(Polyomino(size, tile_matrix=matrix, color=color))

    def populate_bag(self):
        pieces = []
        while len(pieces) < 5:
            pieces += self.polyomino_set
        random.shuffle(pieces)
        self.bag += pieces

    def draw_piece(self):
        if len(self.bag) < 5:
            self.populate_bag()
        return self.bag.pop(0)
