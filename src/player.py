from pygame import K_SPACE, K_UP, K_LEFT, K_RIGHT, K_w, K_s, K_a, K_d
from pygame import Surface, Rect
from pygame.sprite import Group, Sprite

from .camera import Camera
from .constants import HEIGHT, PLAYER_SIZE, PLAYER_COLOR
from .plataform import Platform


class Player(Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image: Surface = Surface(PLAYER_SIZE)
        self.image.fill(PLAYER_COLOR)
        self.rect: Rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_y: float = 0
        self.jumping = False

    def update(self, keys, platforms: Group, camera: Camera):
        # Movement
        speed = 5
        if keys[K_LEFT] or keys[K_a]:
            self.rect.x -= speed
        if keys[K_RIGHT] or keys[K_d]:
            self.rect.x += speed

        # Gravity
        self.vel_y += 0.5  # Simulates gravity
        if self.vel_y > 10:  # Terminal velocity
            self.vel_y = 10
        self.rect.y += int(self.vel_y)

        # Platform collision
        for platform in platforms:
            platform_rect = Rect(
                platform.rect.x - camera.offset_x,
                platform.rect.y - camera.offset_y,
                platform.rect.width,
                platform.rect.height,
            )
            if self.rect.colliderect(platform_rect) and self.vel_y > 0:
                self.rect.bottom = platform_rect.top
                self.vel_y = 0
                self.jumping = False

        # Jumping
        if keys[K_SPACE] or keys[K_UP] and not self.jumping:
            self.vel_y = -20
            self.jumping = True

        # Prevent falling through the floor
        if self.rect.bottom > HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.jumping = False


# Create Player
player: Player = Player(100, HEIGHT - 150)
player_group: Group = Group()
player_group.add(player)
