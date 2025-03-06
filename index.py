import pygame
from constants import WIDTH, HEIGHT, FPS
from player import player, player_group
from plataform import platforms, Platform
from camera import Camera
from sys import exit

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mario')
clock = pygame.time.Clock()
running = True
camera = Camera(WIDTH, HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((135, 206, 235))
    keys = pygame.key.get_pressed()
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
