from images import BIRD_IMAGES
import pygame


class Bird:
    IMAGES = BIRD_IMAGES
    NUMBER_IMAGES = 3
    ANIMATION_TIME = 5

    MAX_IMAGE_COUNT = ANIMATION_TIME * NUMBER_IMAGES

    MAX_ROTATION = 25
    ROTOTATION_VELOCITY = 25

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tilt_count = 0
        self.velocity = 0
        self.height = self.y
        self.image_count = 0
        self.image = IMAGES[0]

    def jump(self):
        self.velocity = -10.5
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
                self.tilt = ROTOTATION_VELOCITY

    def draw(self, window):
        is_current_cycle_increasing = True

        # 0 <= bird_image_number < 2 since 0 <= image_count < 15
        bird_image_number = image_count // ANIMATION_TIME
        self.image = IMAGES[bird_image_number]

        if is_current_cycle_increasing:
            self.image_count += 1
            if self.image_count == MAX_IMAGE_COUNT-1:
                is_current_cycle_increasing = False
        else:
            self.image_count -= 1
            if self.image_count == 0:
                is_current_cycle_increasing = True

        if self.tilt <= -80:
            self.image = IMAGES[1]
            self.image_count = self.ANIMATION_TIME * 2
            is_current_cycle_increasing = True

        rotated_image = pygame.transform.roate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(
            center=self.img.get_rect(topLeft=(self.x, self.y)).center)
        window.blit(rotated_image, new_rect.topLeft)

        def get_mask(self):
            return pygame.mask.from_surface(self.image)
