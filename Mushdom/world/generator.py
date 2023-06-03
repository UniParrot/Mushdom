import pygame
import random

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
    def __init__(self):
        self.width = 500
        self.height = 500
        self.tree_amount = 10
        self.random_distance = 0
        self.tree_group = pygame.sprite.Group()
        self.tree_test = None
        self.random_distance_x = random.randint(0, 300)
        self.random_distance_y = random.randint(0, 300)
    def plant_tree(self):
        for i in range(10):
            self.random_distance_x = random.randint(0, 300)
            self.random_distance_y = random.randint(0, 300)
            self.tree_test = Tree()
            self.tree_test.rect.x = self.random_distance_x
            self.tree_test.rect.y = self.random_distance_y
            self.tree_group.add(self.tree_test)
        return self.tree_group

if __name__ == "__main__" :
    loop = True
    test_world = World()
    screen = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        screen.fill((255,255,255))
        tree_group = test_world.plant_tree()
        if len(tree_group) >= 10 :
            tree_group.kill()
        tree_group.draw(screen)
        pygame.display.update()