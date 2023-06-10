import pygame
import mushroom

background_color = (70, 70, 70)


class Mob(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.captured = None
        self.object_pos_x = None
        self.object_pos_y = None
        self.image_path = "asset/rabbit_left.png"  # default image, can be modified
        self.image = pygame.image.load(self.image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.position_x = position_x
        self.position_y = position_y
        self.radius = 10
        self.ratio = 4
        self.side = 1
        self.image = pygame.transform.scale(self.image, size=(self.width * self.ratio, self.height * self.ratio))
        self.surface = pygame.Surface((self.width * self.ratio, self.height * self.ratio))
        self.surface.blit(self.image, (0, 0))
        self.surface.set_colorkey((0, 0, 255))
        self.rect = self.surface.get_rect()

    def detect(self, object_pos_x, object_pos_y):
        self.object_pos_x = object_pos_x
        self.object_pos_y = object_pos_y
        if (self.object_pos_x ^ 2 + self.object_pos_y ^ 2) > self.radius ^ 2:
            print("detected")

    def captured(self, captured: mushroom.Mushroom):
        self.captured = captured


if __name__ == "__main__":
    TestMob = Mob(0, 0)
    loop = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((720, 480))
    pygame.display.init()
    WHITE = (255, 255, 255)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        screen.fill(background_color)
        screen.blit(TestMob.surface, (0, 0))
        pygame.display.update()
        clock.tick(60)
