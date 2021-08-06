import pygame
import random

from constants import WINDOW_HEIGHT, BASE_HEIGHT, WINDOW_WIDTH
from images import (PIPE_IMAGE_TOP,
                    PIPE_IMAGE_BOTTOM,
                    PIPE_IMAGE_HEIGHT
                    )


def get_random_gap():
    return random.randrange(150, 220)

def random_x_pipe():
    return random.randrange(WINDOW_WIDTH-80, WINDOW_WIDTH)

class Pipe:
    VELOCITY = 5

    def __init__(self):
        self.x = random_x_pipe()
        self.height = 0
        self.gap = 100
        self.PIPE_BOTTOM = PIPE_IMAGE_BOTTOM
        self.PIPE_TOP = PIPE_IMAGE_TOP
        self.top = 0
        self.bottom = 0
        self.passed = False
        self.set_height()

    def set_height(self):
        curr_gap = get_random_gap()
        self.height = random.randrange(0, BASE_HEIGHT - curr_gap)
        self.top = self.height - PIPE_IMAGE_HEIGHT
        self.bottom = self.height + curr_gap

    def move(self):
        self.x -= self.VELOCITY

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
