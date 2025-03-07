from typing import Dict, Tuple


HEIGHT: int = 640
WIDTH: int = 480

FPS: int = 60

TILE_SIZE: int = 16
PLAYER_SIZE: Tuple = (8, 8)
PLAYER_COLOR: Tuple = (255, 0, 122)
PLATFORM_COLOR: Tuple = (0, 122, 80)
BACKGROUND_COLOR: Tuple = (136, 206, 235)
COLORS: Dict[str, Tuple] = {
    'C': (255, 255, 255),
    '#': (0, 200, 0),
    '': BACKGROUND_COLOR
}
