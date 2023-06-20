import pygame
import random
import math

detected_area = None


class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("asset/tree.png")
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.ratio = 3
        self.image = pygame.transform.scale(self.image, (self.width * self.ratio, self.height * self.ratio))
        self.surface = pygame.Surface((self.width * self.ratio, self.height * self.ratio))
        self.surface.set_colorkey((0, 0, 0))
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
    def __init__(self, width, height, pos_list: list):
        super().__init__()
        self.mushroom = None
        self.mob_count = None
        self.pos_x = 0
        self.pos_y = 0
        self.width = width
        self.height = height
        self.pos_list = pos_list
        self.surface = pygame.surface.Surface((self.width, self.height))
        self.rect_inner = pygame.Rect(self.width, self.width, self.width, self.width)
        self.rect_inner.center = [self.width / 2, self.height / 2]
        self.image = pygame.image.load("asset/grass-1.png")
        self.image = pygame.transform.scale(self.image, size=(self.width, self.height))
        self.rect = self.surface.get_rect()
        self.rect.topleft = pos_list[0]
        self.rect.topright = pos_list[1]
        self.rect.bottomleft = pos_list[2]
        self.rect.bottomright = pos_list[3]
        self.mushroom = None
        print(self.color_palette)

    def sides(self, mushroom):
        self.mushroom = mushroom

def generate_area(world_width: int, world_height: int, ratio: int):
    rect_point_upper_right = [0, 0]
    rect_point_upper_left = [0, 0]
    rect_point_bottom_right = [0, 0]
    rect_point_bottom_left = [0, 0]
    world_width = int(world_width)
    world_height = int(world_height)
    area_width = math.gcd(world_width, world_height) / ratio
    print("area_width:", area_width)
    area_height = math.gcd(world_width, world_height) / ratio
    print("area_height:", area_height)
    area_width_amount = int(world_width / area_width)
    print("area_width_amount:", area_width_amount)
    area_height_amount = int(world_height / area_height)
    print("area_height_amount:", area_height_amount)
    area_list = pygame.sprite.Group()
    area = [[0, 0], [0, 0], [0, 0], [0, 0]]
    rect_point_upper_right[0] += area_width
    print("rect_point_upper_right:", rect_point_upper_right)
    rect_point_bottom_left[1] += area_height
    print("rect_point_bottom_left:", rect_point_bottom_left)
    rect_point_bottom_right[0] += area_width
    print("rect_point_bottom_right:", rect_point_bottom_right)
    rect_point_bottom_right[1] += area_height
    print("rect_point_bottom_right:", rect_point_bottom_right)
    for i in range(area_height_amount):
        rect_point_upper_left[0] = 0
        rect_point_upper_right[0] = 0
        rect_point_bottom_left[0] = 0
        rect_point_bottom_right[0] = 0
        for j in range(area_width_amount):
            rect_point_upper_left[0] += area_width
            rect_point_upper_right[0] += area_width
            rect_point_bottom_left[0] += area_width
            rect_point_bottom_right[0] += area_width
            area[0] = rect_point_upper_left
            area[1] = rect_point_upper_right
            area[2] = rect_point_bottom_left
            area[3] = rect_point_bottom_right
            area_list.add(Area(area_width, area_height, area))
            print(area)
        rect_point_upper_left[1] += area_height
        rect_point_upper_right[1] += area_height
        rect_point_bottom_left[1] += area_height
        rect_point_bottom_right[1] += area_height

    print(area_list)
    return area_list


if __name__ == "__main__":
    loop = True
    test_world = World(500, 600)
    screen = pygame.display.set_mode((500, 600))

    area_list = generate_area(500, 600, 2)
    print("world_size: 500, 500")
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        screen.fill((255, 255, 255))
        object_posx, object_posy = pygame.mouse.get_pos()
        for search_area in area_list:
            if search_area.rect.collidepoint(object_posx, object_posy):
                print(search_area.rect.center)
                detected_area = search_area
        area_list.draw(screen)

        pygame.display.update()
