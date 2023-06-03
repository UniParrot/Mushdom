import pygame
BLUE = (0, 0, 255)
class Mushroom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ratio = 5
        self.image = pygame.image.load("asset/mushroom.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.width*self.ratio, self.height*self.ratio))
        self.image.set_colorkey((0,255,0))
        self.surface = pygame.Surface((self.width*self.ratio, self.height*self.ratio))
        self.surface.blit(self.image, (0, 0))
        self.side = None
        self.rect = self.surface.get_rect()

    def update(self):
        for event_ in pygame.event.get():
            if event_.type == pygame.KEYDOWN:
                if event_.key == pygame.K_UP:
                    self.rect.y += 10
                elif event_.key == pygame.K_DOWN:
                    self.rect.y -= 10
                elif event_.key == pygame.K_LEFT:
                    self.rect.x -= 10
                elif event_.key == pygame.K_RIGHT:
                    self.rect.x += 10
class Spore(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((16, 16))
        self.surface.set_colorkey(BLUE)
if __name__ == "__main__":
    TestMushroom = Mushroom()
    TestMushroomGroup = pygame.sprite.Group()
    TestMushroomGroup.add(TestMushroom)
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

        TestMushroom.update()
        TestMushroomGroup.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)