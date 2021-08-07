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

pygame.font.init()  # init font

STAT_FONT = pygame.font.SysFont("roobert", 50)


gen = 0
bestScore = 0

def draw_window(window, birds, not_passed_pipes, passed_pipes, base, score):
    window.blit(BG_IMAGE, (0, 0))

    for pipe in not_passed_pipes:
        pipe.draw(window)

    for pipe in passed_pipes:
        pipe.draw(window)

    score_label = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    window.blit(score_label, (WINDOW_WIDTH - score_label.get_width() - 25, 25))

    best_label = STAT_FONT.render("Best Score: " + str(bestScore), 1, (255, 255, 255))
    window.blit(best_label, (WINDOW_WIDTH - best_label.get_width() - 25, 75))

    gen_label = STAT_FONT.render("Gen: " + str(gen), 1, (255, 255, 255))
    window.blit(gen_label, (25, 25))

    alive_label = STAT_FONT.render("Alive: " + str(len(birds)), 1, (255, 255, 255))
    window.blit(alive_label, (25, 75))

    base.draw(window)

    for bird in birds:
        bird.draw(window)

    pygame.display.update()


def eval_genomes(genomes, config):

    global bestScore, gen

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    birds = []
    bird_genomes = []
    NNs = []

    for _, genome in genomes:
        print(genome)
        genome.fitness = 0  # start with fitness level of 0
        NN = neat.nn.FeedForwardNetwork.create(genome, config)
        NNs.append(NN)
        birds.append(Bird(WINDOW_WIDTH // 5, WINDOW_HEIGHT // 3))
        bird_genomes.append(genome)

    base = Base()
    not_passed_pipes = [Pipe()]
    passed_pipes = []
    score = 0

    while len(birds) > 0:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                # break

        if len(passed_pipes) > 0:
            last_passed_pipe = passed_pipes[-1]
        else:
            last_passed_pipe = None

        first_not_passed_pipe = not_passed_pipes[0]

        birdsX = birds[0].x

        for pipe in not_passed_pipes:
            for bird_index, bird in enumerate(birds):
                if (bird.is_dead(last_passed_pipe, first_not_passed_pipe)):
                    # run = False
                    bird_genomes[bird_index].fitness -= 0.1
                    NNs.pop(bird_index)
                    bird_genomes.pop(bird_index)
                    birds.pop(bird_index)
                else:
                    # output = NNs[bird_index].activate((bird.y, pipe.height, pipe.bottom))
                    # output = NNs[bird_index].activate((bird.y, abs(bird.y - pipe.height), abs(bird.y - pipe.bottom)))

                    fnpp = first_not_passed_pipe

                    # output = NNs[bird_index].activate(
                    #     (bird.y, fnpp.height, fnpp.bottom, fnpp.velocity, fnpp.gap, fnpp.x))      

                    # output = NNs[bird_index].activate(
                    #     (bird.y, fnpp.height, fnpp.bottom))    
                    output = NNs[bird_index].activate(
                        (bird.y, fnpp.height, fnpp.bottom))    
                    
                    # we use a relu activation function so result will be between 0 and +oo. if over 0 jump
                    if output[0] > 50:
                        bird.jump()

                    # we use a relu activation function so result will be between 0 and +oo. if over 0 jump
                    # if output[0] > 0.5:
                    #     bird.jump()

                    bird_genomes[bird_index].fitness += 0.5
                    bird.move()
            pipe.move()

        if len(passed_pipes) > 0:
            for pipe in passed_pipes:
                pipe.move()
            first_passed_pipe = passed_pipes[0]
            if (first_passed_pipe.x < -PIPE_IMAGE_WIDTH):
                passed_pipes.pop(0)

        if (first_not_passed_pipe.x + PIPE_IMAGE_WIDTH / 1.5 < birdsX):
            passed_pipes.append(not_passed_pipes.pop(0))
            not_passed_pipes.append(Pipe())
            score += 1

            if bestScore < score:
                bestScore = score


        draw_window(window, birds, not_passed_pipes, passed_pipes, base, score)
    gen += 1

def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(eval_genomes, 50)

    # show final stats
    # print('\nBest genome:\n{!s}'.format(winner))
    # print('end')


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
