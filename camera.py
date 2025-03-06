class Camera:
    def __init__(self, width, height):
        self.offset_x = 0
        self.offset_y = 0
        self.width = width
        self.height = height

    def update(self, target):
        """ Smoothly move the camera towards the player with a delay """
        target_x = target.rect.centerx - self.width // 2  # Center on player
        target_y = target.rect.centery - self.height // 2

        # Smooth interpolation (LERP-like effect)
        self.offset_x += (target_x - self.offset_x) * 0.1
        self.offset_y += (target_y - self.offset_y) * 0.1
