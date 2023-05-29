"""
mole.py is a file that contains the class for a mole in the game
"""
import random
import pygame

class Mole(pygame.sprite.Sprite):
    "The mole is something the players hit in order to score points"

    # TODO: MAKE THE MOLE BIGGER

    def __init__(self):
        self.on_screen = False
        self.points = 1
        self.waiting = True
        self.wait = 40
        self.time = 0
        self.image = pygame.Surface([240, 240])
        self.image.fill([101, 67, 33])
        self.coord_x = 510
        self.coord_y = 400

    def update(self, game, p1, p2):
        "All mole related updates"
        if self.waiting:
            self.time += 100 * game.delta_time
            if self.time >= self.wait:
                self.waiting = False
        else:
            if not self.on_screen:
                if random.randint(1, 750) == 1:
                    if p1.state == "up" and p2.state == "up":
                        self.on_screen = True

    def hit(self):
        "Method for the mole being hit"

        # TODO: HAVE DIFFERENT MOLE TYPES (RABBIT, MOLE W/HELMET, GOLDEN MOLE, ETC)

        if self.on_screen:
            self.on_screen = False
            self.time = 0
            self.waiting = True

    def draw(self, surface):
        "Pass in a surface to draw the mole onto"
        if self.on_screen:
            surface.blit(self.image, [self.coord_x, self.coord_y])
