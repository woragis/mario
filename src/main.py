from sys import exit

import pygame
from pygame.key import get_pressed as get_key_pressed
from pygame.event import get as get_event

from src.camera import Camera
from src.constants import WIDTH, HEIGHT, FPS
from src.plataform import platforms
from src.player import player, player_group


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mario')
    clock = pygame.time.Clock()
    running = True
    camera = Camera(WIDTH, HEIGHT)

    while running:
        for event in get_event():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((135, 206, 235))
        keys = get_key_pressed()
        player.update(keys, platforms, camera)

        camera.update(player)

        # draw elements relative to the camera
        for platform in platforms:
            screen.blit(platform.image, (platform.rect.x -
                        camera.offset_x, platform.rect.y - camera.offset_y))

        player_group.draw(screen)
        # screen.blit(player.image, (player.rect.x - camera.offset_x,
        #             player.rect.y - camera.offset_y))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    exit(0)
