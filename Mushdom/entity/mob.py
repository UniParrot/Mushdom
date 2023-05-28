import pygame

class Mob(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.object_pos_x = None
        self.object_pos_y = None
        self.image_path = "asset/rabbit.gif" #default image, can be modified
        self.image = pygame.image.load(self.image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.surface = pygame.Surface((self.width, self.height))
        self.position_x = position_x
        self.position_y = position_y
        self.radius = 10
        self.side = 1

    def detect(self, object_pos_x, object_pos_y):
        self.object_pos_x = object_pos_x
        self.object_pos_y = object_pos_y
        if (self.object_pos_x ^ 2 + self.object_pos_y ^ 2) > self.radius ^ 2:
            print("detected")

