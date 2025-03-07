from typing import Dict, Tuple


HEIGHT: int = 640
WIDTH: int = 480

FPS: int = 60

PLAYER_SIZE: Tuple = (8, 8)
PLAYER_COLOR: Tuple = (255, 0, 122)
TILE_SIZE: int = 16
BACKGROUND_COLOR: Tuple = (136, 206, 235)
COLORS: Dict[str, Tuple] = {
    'C': (255, 255, 255),
    '#': (0, 200, 0),
    '': BACKGROUND_COLOR
}
