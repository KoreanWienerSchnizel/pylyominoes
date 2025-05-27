import pygame
from pygame.color import Color

from bag import Bag
from constants import (
    CLASSIC_COLORS,
    CLASSIC_PIECES,
    COMBO_MULT,
    GRID_BUFFER_HEIGHT,
    GRID_BUFFER_ROW,
    GRID_OFFSET_X,
    GRID_OFFSET_Y,
    LIVE_TIME,
    PREVIEW_SIZE,
    PYLYO_SCORE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TILE_SIZE,
    Move,
)
from grid import Grid


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.background_color = Color("0x1d2d44")

        self.live_piece = None
        self.game_grid = None
        self.bag = None
        self.difficulty = None

        self.combo = 0
        self.total_lines_cleared = 0
        self.total_score = 0
        self.game_over = False

    def classic_game(self):
        self.game_grid = Grid()
        self.bag = Bag(list(CLASSIC_PIECES.values()), list(CLASSIC_COLORS.values()))
        self.preview_surface = pygame.surface.Surface((PREVIEW_SIZE, PREVIEW_SIZE))
        self.difficulty = 1000
        game_tick = self.difficulty

        self.new_piece()
        live_dt = LIVE_TIME
        while not self.game_over:
            game_tick -= self.dt
            if game_tick <= 0:
                force_move = self.live_piece.move(Move.DOWN, self.game_grid)
                if force_move:
                    game_tick = self.difficulty
                else:
                    game_tick = 0
                    live_dt -= self.dt
                    if live_dt <= 0 and not force_move:
                        self.place_piece()
                        live_dt = LIVE_TIME

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_over = True

                    if event.key == pygame.K_SPACE:
                        if not self.live_piece.move(Move.DOWN, self.game_grid):
                            self.place_piece()
                            live_dt = LIVE_TIME
                        else:
                            while self.live_piece.move(Move.DOWN, self.game_grid):
                                continue
                            live_dt = LIVE_TIME
                            game_tick = self.difficulty

                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.live_piece.rotate(self.game_grid)
                        live_dt = LIVE_TIME

                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        game_tick = self.difficulty
                        can_move = self.live_piece.move(Move.DOWN, self.game_grid)
                        if not can_move:
                            self.place_piece()
                            live_dt = LIVE_TIME

                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.live_piece.move(Move.LEFT, self.game_grid)
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.live_piece.move(Move.RIGHT, self.game_grid)

            self.screen.fill(self.background_color)
            self.game_grid.update()
            self.live_piece.draw(self.game_grid.grid_surface)
            self.game_grid.draw(self.screen)
            self.draw_score()
            self.draw_piece_preview(self.preview_surface)

            pygame.display.flip()
            self.dt = self.clock.tick()

    def place_piece(self):
        lines_cleared = self.game_grid.place_piece(self.live_piece)
        self.new_piece()
        print(f"place_piece: {lines_cleared}")
        if lines_cleared == 0:
            self.combo = 0
            return
        if lines_cleared < 0:
            self.game_over = True
            return
        score = PYLYO_SCORE if lines_cleared >= 4 else 0
        score += lines_cleared * 10
        score = score * (1 + (self.combo * COMBO_MULT))
        self.combo += 1
        self.total_lines_cleared += lines_cleared
        self.total_score += int(score)

    def new_piece(self):
        self.live_piece = self.bag.draw_piece()
        self.live_piece.coord = (
            (self.game_grid.col // 2) - (len(self.live_piece.tile_matrix[0]) // 2),
            (GRID_BUFFER_ROW - len(self.live_piece.tile_matrix)),
        )
        for i in range(len(self.live_piece.tile_matrix) - 1, 0, -1):
            if any(self.live_piece.tile_matrix[i]):
                break
            self.live_piece.coord = (
                self.live_piece.coord[0],
                self.live_piece.coord[1] + 1,
            )
        self.live_piece.tiles = self.live_piece.get_tiles()
        pygame.event.clear()

    def draw_piece_preview(self, surface):
        surface.fill("0x3e5c76")
        pygame.draw.rect(surface, "white", surface.get_rect(), width=1)
        self.live_piece.draw_preview(surface)
        self.screen.blit(
            surface,
            (
                GRID_OFFSET_X + (self.game_grid.col * TILE_SIZE),
                GRID_OFFSET_Y + GRID_BUFFER_HEIGHT,
            ),
        )

    def draw_score(self):
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = [
            f"SCORE: {self.total_score}",
            f"LINES: {self.total_lines_cleared}",
        ]
        text_render = []
        for i in range(len(text)):
            text_render.append(font.render(text[i], True, "white"))
        x = GRID_OFFSET_X + (self.game_grid.col * TILE_SIZE) + PREVIEW_SIZE + 5
        y = GRID_OFFSET_Y + GRID_BUFFER_HEIGHT
        for i in range(len(text_render)):
            self.screen.blit(text_render[i], (x, y))
            y += text_render[i].get_height() + 2
