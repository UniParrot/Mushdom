import pygame
import mushroom
import math
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
        self.radius = 300
        self.ratio = 4
        self.side = 1
        self.image = pygame.transform.scale(self.image, size=(self.width * self.ratio, self.height * self.ratio))
        self.image.set_colorkey((0, 0, 255))
        self.surface = pygame.Surface((self.width * self.ratio, self.height * self.ratio))
        self.surface.blit(self.image, (0, 0))
        self.rect = self.surface.get_rect()
        self.skill_key = pygame.K_e
        self.rect.x = position_x
        self.rect.y = position_y
        self.object_pos_x = 0
        self.object_pos_y = 0
        self.distance = float(self.object_pos_x - self.rect.centerx) ** 2 + (self.object_pos_y - self.rect.centery) ** 2
        print(self.rect.center)

    def detect(self, object_pos_x, object_pos_y):
        self.object_pos_x = object_pos_x
        self.object_pos_y = object_pos_y
        print(self.distance)
        if self.distance < self.radius**2:
            print("detected")
        else:
            print("Not detected")
    def captured(self, captured: mushroom.Mushroom):
        self.captured = captured

    def is_dismount(self):
        return 0
class Boar(Mob):
    def __init__(self, position_x, position_y):
        super().__init__(position_x=position_x, position_y=position_y)
        self.radius = 80
        self.image = pygame.image.load("asset/boar.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, size=(self.width*self.ratio, self.height*self.ratio))


if __name__ == "__main__":
    MobGroup = pygame.sprite.Group()
    TestMob = Boar(360, 240)
    loop = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((720, 480))
    pygame.display.init()
    MobGroup.add(TestMob)
    WHITE = (255, 255, 255)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        pos_x, pos_y = pygame.mouse.get_pos()
        TestMob.detect(pos_x, pos_y)
        screen.fill(background_color)
        MobGroup.draw(screen)
        pygame.display.update()
        clock.tick(60)
