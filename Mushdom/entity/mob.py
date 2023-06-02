import pygame
import mushroom
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
        self.surface.blit(self.image, (0, 0))

    def detect(self, object_pos_x, object_pos_y):
        self.object_pos_x = object_pos_x
        self.object_pos_y = object_pos_y
        if (self.object_pos_x ^ 2 + self.object_pos_y ^ 2) > self.radius ^ 2:
            print("detected")
        
    def captured(self, capturer : mushroom.Mushroom):
        self.capturer = capturer
        

if __name__ == "__main__":
    pos_x = 1
    pos_y = 2
    TestMushroom = Mob(pos_x, pos_y)
    loop = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((720, 480))
    pygame.display.init()
    WHITE = (255, 255, 255)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        screen.fill(WHITE)
        screen.blit(TestMushroom.surface, (pos_x, pos_y))
        pygame.display.update()
