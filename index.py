import pygame
from sys import exit


class GameObject:
    def __init__(self, image, height, speed):
        self.image = image
        self.pos = image.get_rect().move(0, height)
        self.speed = speed

    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0


pygame.init()
clock = pygame.time.Clock()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
player = pygame.image.load('assets/compa_idle.png').convert()
background = pygame.image.load('assets/background.jpg').convert()
screen.blit(background, (0, 0))
objects = []

for x in range(10):
    o = GameObject(player, x*40, x)
    objects.append(o)

running = True
dt = 0

player_pos = pygame.Vector2(
    screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)

        # screen.fill('white')

        # pygame.draw.circle(screen, 'red', player_pos, 40)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     player_pos.y += 300*dt
        # if keys[pygame.K_s]:
        #     player_pos.y -= 300*dt
        # if keys[pygame.K_a]:
        #     player_pos.x -= 300*dt
        # if keys[pygame.K_d]:
        #     player_pos.x += 300*dt

        pygame.display.update()

        # dt = clock.tick(60) / 1000
        # player_pos.y += 100*dt
        clock.tick(60)

pygame.quit()
exit(0)
