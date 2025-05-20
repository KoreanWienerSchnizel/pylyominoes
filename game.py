import pygame
from pygame.color import Color

from bag import Bag
from constants import (
    CLASSIC_COLORS,
    CLASSIC_PIECES,
    GRID_BUFFER_ROW,
    LIVE_TIME,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    Move,
)
from grid import Grid


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        dt = 0
        background_color = Color("0x1d2d44")
        game_grid = Grid()
        bag = Bag(list(CLASSIC_PIECES.values()), list(CLASSIC_COLORS.values()))
        live_piece = self.new_piece(bag, game_grid)
        live_dt = LIVE_TIME
        difficulty = 1000
        game_tick = difficulty

        running = True
        while running:
            game_tick -= dt
            if game_tick <= 0:
                force_move = live_piece.move(Move.DOWN, game_grid)
                if force_move:
                    game_tick = difficulty
                else:
                    game_tick = 0
                    live_dt -= dt
                    if live_dt <= 0 and not force_move:
                        game_grid.place_piece(live_piece)
                        live_piece = self.new_piece(bag, game_grid)
                        live_dt = LIVE_TIME

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_SPACE:
                        if not live_piece.move(Move.DOWN, game_grid):
                            game_grid.place_piece(live_piece)
                            live_piece = self.new_piece(bag, game_grid)
                            live_dt = LIVE_TIME
                        else:
                            while live_piece.move(Move.DOWN, game_grid):
                                continue
                            live_dt = LIVE_TIME
                            game_tick = difficulty

                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        live_piece.rotate(game_grid)
                        live_dt = LIVE_TIME

                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        game_tick = difficulty
                        can_move = live_piece.move(Move.DOWN, game_grid)
                        if not can_move:
                            game_grid.place_piece(live_piece)
                            live_piece = self.new_piece(bag, game_grid)
                            live_dt = LIVE_TIME

                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        live_piece.move(Move.LEFT, game_grid)
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        live_piece.move(Move.RIGHT, game_grid)

            self.screen.fill(background_color)
            game_grid.update()
            live_piece.draw(game_grid.grid_surface)
            game_grid.draw(self.screen)

            print(live_piece.tiles[0].coord)

            pygame.display.flip()
            dt = self.clock.tick()

    def new_piece(self, bag, grid):
        piece = bag.draw_piece()
        piece.coord = (
            (grid.col // 2) - (len(piece.tile_matrix[0]) // 2),
            (GRID_BUFFER_ROW - len(piece.tile_matrix)),
        )
        piece.tiles = piece.get_tiles()
        return piece
