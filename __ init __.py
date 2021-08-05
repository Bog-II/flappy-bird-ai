import pygame
import neat
import time
import os
import random

import sys

from load_images import load_image

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

BIRD_IMAGES = [
    load_image("images", 'bird1.png'),
    load_image("images", 'bird2.png'),
    load_image("images", 'bird3.png')
]
