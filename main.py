import pygame
import neat
import time
import os


from images import BG_IMAGE, BASE_IMAGE, PIPE_IMAGE_WIDTH
from classes.Bird import Bird
from classes.Pipe import Pipe
from classes.Base import Base
from constants import (WINDOW_WIDTH, WINDOW_HEIGHT,
                       BASE_HEIGHT)


def draw_window(window, bird, not_passed_pipes, passed_pipes, base):
    window.blit(BG_IMAGE, (0, 0))

    for pipe in not_passed_pipes:
        pipe.draw(window)

    for pipe in passed_pipes:
        pipe.draw(window)

    base.draw(window)
    bird.draw(window)

    pygame.display.update()


def main():
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    bird = Bird(WINDOW_WIDTH // 5, WINDOW_HEIGHT // 3)
    base = Base()

    not_passed_pipes = [Pipe()]
    passed_pipes = []

    run = True
    while run:
        clock.tick(30)

        if len(passed_pipes) > 0:
            last_passed_pipe = passed_pipes[-1]
        else:
            last_passed_pipe = None

        first_not_passed_pipe = not_passed_pipes[0]

        if (bird.is_dead(last_passed_pipe, first_not_passed_pipe)):
            run = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    bird.jump()
                if event.type == pygame.QUIT:
                    run = False

            if len(passed_pipes) > 0:
                for pipe in passed_pipes:
                    pipe.move()
                first_passed_pipe = passed_pipes[0]
                if (first_passed_pipe.x < -PIPE_IMAGE_WIDTH):
                    passed_pipes.pop(0)

            bird.move()

            for pipe in not_passed_pipes:
                pipe.move()

            first_not_passed_pipe = not_passed_pipes[0]
            if (first_not_passed_pipe.x < bird.x):
                passed_pipes.append(not_passed_pipes.pop(0))
                not_passed_pipes.append(Pipe())

        draw_window(window, bird, not_passed_pipes, passed_pipes, base)

    pygame.quit()
    quit()


main()
