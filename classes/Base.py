from constants import BASE_HEIGHT
from images import (BASE_IMAGE,
                    BASE_IMAGE_WIDTH)


class Base:
    VELOCITY = 5

    def __init__(self):
        self.y = BASE_HEIGHT
        self.x1 = 0
        self.x2 = BASE_IMAGE_WIDTH

    def draw(self, window):
        window.blit(BASE_IMAGE, (self.x1, self.y))
        window.blit(BASE_IMAGE, (self.x2, self.y))
