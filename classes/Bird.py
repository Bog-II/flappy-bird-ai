from images import BIRD_IMAGES
from constants import BASE_HEIGHT
import pygame


class Bird:
    IMAGES = BIRD_IMAGES
    NUMBER_IMAGES = 3
    ANIMATION_TIME = 5

    MAX_IMAGE_COUNT = ANIMATION_TIME * NUMBER_IMAGES

    MAX_ROTATION = 25
    ROTOTATION_VELOCITY = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tilt_count = 0
        self.velocity = 0
        self.height = y
        self.image_count = 0
        self.image = self.IMAGES[0]
        self.is_current_cycle_increasing = True

    def jump(self):
        self.velocity = -10
        self.tilt_count = 0
        self.height = self.y

    def move(self):
        self.tilt_count += 1

        displacement = self.velocity * self.tilt_count + 1.5 * self.tilt_count ** 2

        if displacement >= 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2

        self.y += displacement

        if (displacement < 0) | (self.y < self.height + 50):
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTOTATION_VELOCITY

    def draw(self, window):

        # 0 <= bird_image_number < 2 since 0 <= image_count < 15
        bird_image_number = self.image_count // self.ANIMATION_TIME
        self.image = self.IMAGES[bird_image_number]

        if self.is_current_cycle_increasing:
            self.image_count += 1
            if self.image_count == self.MAX_IMAGE_COUNT-1:
                self.is_current_cycle_increasing = False
        else:
            self.image_count -= 1
            if self.image_count == 0:
                self.is_current_cycle_increasing = True

        if self.tilt <= -80:
            self.image = self.IMAGES[1]
            self.image_count = self.ANIMATION_TIME * 2
            self.is_current_cycle_increasing = True

        rotated_image = pygame.transform.rotate(self.image, self.tilt)
        new_rect = rotated_image.get_rect(
            center=self.image.get_rect(
                topleft=(self.x, self.y)
            ).center
        )

        window.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def is_dead(self, last_passed_pipe, first_not_passed_pipe):

        is_bird_colliding_last_passed_pipe = False
        if (last_passed_pipe != None):
            is_bird_colliding_last_passed_pipe = last_passed_pipe.collide(self)

        is_bird_colliding_pipes = is_bird_colliding_last_passed_pipe | first_not_passed_pipe.collide(
            self)

        is_bird_colliding_floor = (self.y >= BASE_HEIGHT)
        is_bird_colligind_ceil = (self.y <= 0)

        return is_bird_colliding_pipes | is_bird_colliding_floor | is_bird_colligind_ceil
