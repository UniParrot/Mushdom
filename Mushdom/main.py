import pygame
import entity.mushroom
import world

loop = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((720, 480))
pygame.display.init()
WHITE = (255, 255, 255)
key_up = False
key_down = False
key_left = False
key_right = False
TestMushroom = entity.mushroom.Mushroom()
TestMushroomGroup = pygame.sprite.Group()
TestMushroomGroup.add(TestMushroom)

while loop:
    pygame.display.init()
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

    pygame.display.update()
