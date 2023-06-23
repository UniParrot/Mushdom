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
        self.image_front = pygame.image.load("asset/mushroom_front.png")
        self.image_behind = pygame.image.load("asset/mushroom_behind.png")
        self.image_left_normal = pygame.image.load("asset/mushroom_left.png")
        self.image_right_normal = pygame.transform.flip(self.image_left_normal, False, True)
        self.image_left_walk = pygame.image.load("asset/mushroom_left_walk.png")
        self.image_right_walk = pygame.transform.flip(self.image_left_walk, False, True)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.width*self.ratio, self.height*self.ratio))
        self.image.set_colorkey((0, 255, 0))
        self.surface = pygame.Surface((self.width*self.ratio, self.height*self.ratio))
        self.side = None
        self.rect = self.surface.get_rect()
        self.spore_count = 10
        self.image_side = "front"
        self.surface.blit(self.image_front, (0, 0))
    def walking(self, direction : string):
        self.image_side = direction
        if self.image_side == "front":
            self.surface.blit(self.image_front, (0, 0))
        elif self.image_side == "behind":
            self.surface.blit(self.image_behind, (0, 0))
        elif self.image_side == "left":
            self.surface.blit(self.image_left_normal, (0, 0))
        elif self.image_side == "right":
            self.surface.blit(self.image_right_normal, (0, 0))
        elif self.image_side == "right walk":
            self.surface.blit(self.image_right_walk, (0, 0))
        elif self.image_side == "left walk":
            self.surface.blit(self.image_left_walk, (0, 0))
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
                    TestMushroom.walking("behind")
                elif event.key == pygame.K_DOWN:
                    key_down = True
                    TestMushroom.walking("front")
                elif event.key == pygame.K_LEFT:
                    key_left = True
                    TestMushroom.walking("left walk")
                elif event.key == pygame.K_RIGHT:
                    key_right = True
                    TestMushroom.walking("front walk")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    key_up = False
                    TestMushroom.walking("behind")
                elif event.key == pygame.K_DOWN:
                    key_down = False
                    TestMushroom.walking("front")
                elif event.key == pygame.K_LEFT:
                    key_left = False
                    TestMushroom.walking("left")
                elif event.key == pygame.K_RIGHT:
                    key_right = False
                    TestMushroom.walking("right")
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
