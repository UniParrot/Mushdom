import pygame
BLUE = (0, 0, 255)
class Mushroom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((32, 32))
        self.image = pygame.image.load("asset/mushroom.png")
        self.surface.set_colorkey(BLUE)
        self.surface.blit(self.image, (0, 0))
        self.side = None


if __name__ == "__main__":
    TestMushroom = Mushroom()
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
        screen.blit(TestMushroom.surface, (0, 0))
        pygame.display.update()
