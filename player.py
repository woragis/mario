import pygame
from constants import HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))  # Character size
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_y = 0  # Vertical velocity
        self.jumping = False

    def update(self, keys, platforms):
        # Movement
        speed = 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed

        # Gravity
        self.vel_y += 0.5  # Simulates gravity
        if self.vel_y > 10:  # Terminal velocity
            self.vel_y = 10
        self.rect.y += self.vel_y

        # Platform collision
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.jumping = False

        # Jumping
        if keys[pygame.K_SPACE] and not self.jumping:
            self.vel_y = -10
            self.jumping = True

        # Prevent falling through the floor
        if self.rect.bottom > HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.jumping = False


# Create Player
player = Player(100, HEIGHT - 150)
player_group = pygame.sprite.Group()
player_group.add(player)
