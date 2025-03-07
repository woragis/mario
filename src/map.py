# Draw map
import pygame

from .constants import TILE_SIZE, COLORS


def load_map(filename: str):
    with open(filename, 'r') as file:
        return [line.strip('\n') for line in file.readlines()]


def draw_map(game_map, screen, char):
    for row_index, row in enumerate(game_map):
        for col_index, col in enumerate(row):
            if char in COLORS:
                color = COLORS[char]
                pygame.draw.rect(screen, color,
                                 (col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))
