import pygame

class Territory(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.width = None
        self.height = None
        self.pos_x = position_x
        self.pos_y = position_y
        self.owner = None