import pygame
import random

from constants import WINDOW_HEIGHT
from images import (PIPE_IMAGE_TOP,
                    PIPE_IMAGE_BOTTOM,
                    PIPE_IMAGE_HEIGHT)


class Pipe:
    GAP = 200
    VELOCITY = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 100

        self.PIPE_TOP = PIPE_IMAGE_TOP,
        self.PIPE_BOTTOM = PIPE_IMAGE_BOTTOM

        self.top = 0
        self.bottom = 0

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, WINDOW_HEIGHT - 100)
        self.top = self.height - PIPE_IMAGE_HEIGHT
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.vel

    def draw(self, window):
        window.blit(self.PIPE_IMAGE_TOP, (self.x, self.top))
        window.blit(self.PIPE_IMAGE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird) -> bool:
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_IMAGE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_IMAGE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        tPoint = bird_mask.overlap(top_mask, top_offset)
        bPoint = bird_mask.overlap(bottom_mask, bottom_offset)

        if (tPoint or bPoint):
            return True

        return False
