import pygame
import neat
import time
import os
import random

from images import BG_IMAGE, BASE_IMAGE
from classes.Bird import Bird

from constants import (WINDOW_WIDTH, WINDOW_HEIGHT)



def draw_window(window, bird):
    window.blit(BG_IMAGE, (0, 0))
    bird.draw(window)
    pygame.display.update()


def main():
    bird = Bird(200, 200)
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run = False

        bird.move()
        draw_window(window, bird)
        # draw_window(window)
    

    pygame.quit()
    quit()

main()