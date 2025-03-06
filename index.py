import pygame
from constants import WIDTH, HEIGHT, FPS
from player import player, player_group
from plataform import platforms, Platform
from sys import exit

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mario')
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((135, 206, 235))
    keys = pygame.key.get_pressed()
    player.update(keys, platforms)

    player_group.draw(screen)
    platforms.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit(0)
