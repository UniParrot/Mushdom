import pygame
BLUE = (0, 0, 255)

key_up = False
key_down = False
key_left = False
key_right = False


class Mushroom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.screen_ = None
        self.ratio = 5
        self.image = pygame.image.load("asset/mushroom.png")

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.width*self.ratio, self.height*self.ratio))
        self.image.set_colorkey((0, 255, 0))
        self.surface = pygame.Surface((self.width*self.ratio, self.height*self.ratio))
        self.surface.blit(self.image, (0, 0))
        self.side = None

        self.rect = self.surface.get_rect()


    def update(self):
        for event_ in pygame.event.get():
            if event_.type == pygame.KEYDOWN:
                if event_.key == pygame.K_UP:
                    self.velocity = pygame.math.Vector2((200, 200)) * 10
                elif event_.key == pygame.K_DOWN:
                    self.velocity-= 10
                elif event_.key == pygame.K_LEFT:
                    self.velocity -= 10
                elif event_.key == pygame.K_RIGHT:
                    self.velocity += 10
            self.position = self.position * self.velocity

    def draw(self, screen_ : pygame.Surface):
        self.screen_ = screen_
        self.screen_.blit(self.surface, (self.rect.x, self.rect.y))


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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    key_up = True

                elif event.key == pygame.K_DOWN:
                    key_down = True

                elif event.key == pygame.K_LEFT:
                    key_left = True

                elif event.key == pygame.K_RIGHT:
                    key_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    key_up = False

                elif event.key == pygame.K_DOWN:
                    key_down = False

                elif event.key == pygame.K_LEFT:
                    key_left = False

                elif event.key == pygame.K_RIGHT:
                    key_right = False

        if key_up:
            TestMushroom.rect.y -= 5
        elif key_down:
            TestMushroom.rect.y += 5
        if key_up and key_down:
            key_up = False
            key_down = False
        if key_left:
            TestMushroom.rect.x -= 5
        elif key_right:
            TestMushroom.rect.x += 5
        if key_right and key_left:
            key_right = False
            key_left = False

        screen.fill(WHITE)
        TestMushroomGroup.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
