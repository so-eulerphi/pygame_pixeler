import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
BROWN = (101, 67, 33)

COLOR_MAP = {
    'G': GOLD, 'B': BROWN, 'W': WHITE, '#': BLACK
}

CHEST_PIXELS = [
    "................", "  BBBBBBBBBBBB  ", " BBBBBGGGGGBBBB ", "BBBBGGWWWWGGBBBB",
    "BBBGWWWWWWWWGBBB", "BBGGWWWWWWWWGGBB", "BBGGGGGGGGGGGGBB", "BBBBBBG#GBBBBBBB",
    "BBGGGGG#GGGGGGBB", "BBGGGGGGGGGGGGBB", " BBGGGGGGGGGGBB ", "  BBBBBBBBBBBB  ",
    "................", "................", "................", "................"
]

def create_surface_from_pixels(pixel_map, pixel_size=6):
    rows = len(pixel_map)
    cols = len(pixel_map[0])
    surf = pygame.Surface((cols * pixel_size, rows * pixel_size), pygame.SRCALPHA)

    for r, row in enumerate(pixel_map):
        for c, char in enumerate(row):
            color = COLOR_MAP.get(char)
            if color:
                pygame.draw.rect(surf, color, (c * pixel_size, r * pixel_size, pixel_size, pixel_size))
    return surf