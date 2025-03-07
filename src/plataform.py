import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))  # Green platform
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


# Create platforms
platforms = pygame.sprite.Group()
platforms.add(Platform(200, 500, 200, 20))  # Example platform
