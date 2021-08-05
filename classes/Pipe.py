import pygame
import random

from images import PIPE_IMAGE_TOP, PIPE_IMAGE_BOTTOM
from constants import WINDOW_HEIGHT


class Pipe:
    GAP = 200
    VELOCITY = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 100

        self.top = 0
        self.bottom = 0

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, WINDOW_HEIGHT - 100)
        self.top = self.height - PIPE_IMAGE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.vel

    def draw(self, window):
        window.blit(self.PIPE_IMAGE_TOP, (self.x, self.top))
        window.blit(self.PIPE_IMAGE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
      
