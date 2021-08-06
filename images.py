import pygame
import os
from constants import IMAGE_DIRECTORY_PATH


def load_image(path: str):
    return pygame.transform.scale2x(
        pygame.image.load((os.path.join(IMAGE_DIRECTORY_PATH, path))))


BIRD_IMAGES = [
    load_image("bird1.png"),
    load_image("bird2.png"),
    load_image("bird3.png")
]


BASE_IMAGE = load_image("base.png")
BG_IMAGE = load_image("bg.png")

PIPE_IMAGE_BOTTOM = load_image("pipe.png")
PIPE_IMAGE_TOP = pygame.transform.flip(PIPE_IMAGE_BOTTOM, False, True)

PIPE_IMAGE_HEIGHT = PIPE_IMAGE_BOTTOM.get_height()
PIPE_IMAGE_WIDTH = PIPE_IMAGE_BOTTOM.get_width()

BASE_IMAGE_WIDTH = BASE_IMAGE.get_width()
BASE_IMAGE_HEIGHT = BASE_IMAGE.get_height()
