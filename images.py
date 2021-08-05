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


PIPE_IMAGE = load_image("pipe.png")
BASE_IMAGE = load_image("base.png")
BG_IMAGE = load_image("bg.png")
