import pygame
import os


def load_image(directory: str, path: str):
    return pygame.transform.scale2x(
        pygame.image.load((os.path.join("images", 'bird1.png'))))