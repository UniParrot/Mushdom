import pygame

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

    pygame.display.update()
