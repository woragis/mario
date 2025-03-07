from sys import exit

import pygame
from pygame.key import get_pressed as get_key_pressed
from pygame.event import get as get_event

from src.camera import Camera
from src.constants import WIDTH, HEIGHT, FPS, COLORS, TILE_SIZE, BACKGROUND_COLOR
from src.player import player, player_group
from src.map import load_map


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mario')
    clock = pygame.time.Clock()
    running = True
    camera = Camera(WIDTH, HEIGHT)
    game_map = load_map('src/maps/map-1.txt')

    while running:
        for event in get_event():
            if event.type == pygame.QUIT:
                running = False

        # screen.fill(BACKGROUND_COLOR)

        # Draw background tiles (cloud and other things)
        for row_index, row in enumerate(game_map):
            for col_index, char in enumerate(row):
                if char in COLORS:
                    pygame.draw.rect(screen, COLORS[char],
                                     (col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                else:
                    pygame.draw.rect(screen, COLORS[''],
                                     (col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        # keys = get_key_pressed()
        # player.update(keys, platforms, camera)

        # camera.update(player)

        # # draw elements relative to the camera
        # for platform in platforms:
        #     screen.blit(platform.image, (platform.rect.x -
        #                 camera.offset_x, platform.rect.y - camera.offset_y))

        # player_group.draw(screen)
        # # screen.blit(player.image, (player.rect.x - camera.offset_x,
        # #             player.rect.y - camera.offset_y))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    exit(0)
