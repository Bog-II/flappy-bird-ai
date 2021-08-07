import pygame
import random

from constants import WINDOW_HEIGHT, BASE_HEIGHT, WINDOW_WIDTH, BIRD_SPEED
from images import (PIPE_IMAGE_TOP,
                    PIPE_IMAGE_BOTTOM,
                    PIPE_IMAGE_HEIGHT
                    )


def get_random_gap():
    return random.randrange(180, 220)

def get_random_x_pipe():
    return random.randrange(WINDOW_WIDTH, WINDOW_WIDTH + 30)

def get_random_velocity():
    return BIRD_SPEED + random.randrange(0, BIRD_SPEED)


class Pipe:

    def __init__(self):
        self.velocity = get_random_velocity()
        self.x = get_random_x_pipe()
        self.height = 0
        self.gap = get_random_gap()
        self.PIPE_BOTTOM = PIPE_IMAGE_BOTTOM
        self.PIPE_TOP = PIPE_IMAGE_TOP
        self.top = 0
        self.bottom = 0
        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(0, BASE_HEIGHT - self.gap)
        self.top = self.height - PIPE_IMAGE_HEIGHT
        self.bottom = self.height + self.gap

    def move(self):
        self.x -= self.velocity

    def draw(self, window):
        window.blit(self.PIPE_TOP, (self.x, self.top))
        window.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird) -> bool:
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        tPoint = bird_mask.overlap(top_mask, top_offset)
        bPoint = bird_mask.overlap(bottom_mask, bottom_offset)

        return (tPoint != None) | (bPoint != None)

        # if (tPoint == None) & (bPoint == None):
        #     return False
        # return True
