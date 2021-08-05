import pygame
import neat
import time
import os
import random

import sys

from load_images import load_image

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

IMAGE_DIRECTORY_PATH = "images"

BIRD_IMAGES = [
    load_image(IMAGE_DIRECTORY_PATH, "bird1.png"),
    load_image(IMAGE_DIRECTORY_PATH, "bird2.png"),
    load_image(IMAGE_DIRECTORY_PATH, "bird3.png")
]

PIPE_IMAGE = load_image(IMAGE_DIRECTORY_PATH, "pipe.png")
BASE_IMAGE = load_image(IMAGE_DIRECTORY_PATH, "base.png")
BG_IMAGE = load_image(IMAGE_DIRECTORY_PATH, "bg.png")
