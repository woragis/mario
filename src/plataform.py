from pygame import Surface
from pygame.sprite import Group, Sprite

from .constants import PLATFORM_COLOR


class Platform(Sprite):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(PLATFORM_COLOR)  # Green platform
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


# Create platforms
platforms: Group = Group()
platforms.add(Platform(200, 500, 200, 20))  # Example platform
