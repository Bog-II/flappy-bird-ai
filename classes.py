from images import BIRD_IMAGES


class Bird:
    IMAGES = BIRD_IMAGES
    MAX_ROTATION = 25
    ROTOTATION_VELOCITY = 25
    ANIMATION_TIME = 5

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

        d = self.velocity
