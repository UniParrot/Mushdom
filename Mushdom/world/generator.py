import pygame
import random
import math
class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("asset/tree.png")
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.ratio = 3
        self.image = pygame.transform.scale(self.image, (self.width*self.ratio, self.height*self.ratio))
        self.surface = pygame.Surface((self.width*self.ratio, self.height*self.ratio))
        self.surface.set_colorkey((0,0,0))
        self.surface.blit(self.image, (0, 0))
        self.rect = self.surface.get_rect()

class World:
    def __init__(self, world_width, world_height):
        self.width = world_width
        self.height = world_height
        self.tree_amount = 10
        self.random_distance = 0
        self.tree_group = pygame.sprite.Group()
        self.tree_test = None
        self.random_distance_x = random.randint(0, self.width)
        self.random_distance_y = random.randint(0, self.height)
    def plant_tree(self):
        for i in range(10):
            self.random_distance_x = random.randint(0, self.width)
            self.random_distance_y = random.randint(0, self.height)
            self.tree_test = Tree()
            self.tree_test.rect.x = self.random_distance_x
            self.tree_test.rect.y = self.random_distance_y
            self.tree_group.add(self.tree_test)
        return self.tree_group
class Area(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mushroom = None
        self.mob_count = None
        self.width = None
        self.height = None
def generate_area(world_width, world_height):
    rect_point_upper_right = 0
    rect_point_upper_left = 0
    rect_point_bottom_right = 0
    rect_point_upper_left = 0
    world_width = int(world_width)
    world_height = int(world_height)
    area_width = math.gcd(world_width, world_height)
    area_height = math.gcd(world_width, world_height)
    area_width_amount = world_width / area_width
    area_height_amount = world_height / area_height
if __name__ == "__main__" :
    loop = True
    test_world = World(1920, 1080)
    screen = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
    tree_group = test_world.plant_tree()
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        screen.fill((255,255,255))

        tree_group.draw(screen)
        pygame.display.update()
