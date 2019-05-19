import pygame
from math import pi

RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (225, 225, 0)
BROWN = (150, 75, 0)
STRONG_BLUE = (0, 0, 100)
SIZE = (500, 400)
BALOON_SIZE = 60
CLOUD_SIZE = (150, 90)
SUN_SIZE = 100
K = 0.8
BASKET_COORDINATES = (int(SIZE[0]/2) - K * BALOON_SIZE, int(SIZE[1] / 2) + 1.5 * K * BALOON_SIZE)
BASKET_SIZE = (BALOON_SIZE * 2 * K, 50)

pygame.init()
dis = pygame.display.set_mode(SIZE)

pygame.display.update()

aux_left = 0
aux_right = 0
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    aux_left += 1
    aux_right += 2
    dis.fill(STRONG_BLUE)
    pygame.draw.circle(dis, YELLOW, (SIZE[0] - aux_left, int(SUN_SIZE * 0.8)), BALOON_SIZE * 2)
    pygame.draw.ellipse(dis, WHITE, ((200, 40), CLOUD_SIZE))
    pygame.draw.ellipse(dis, WHITE, ((SIZE[0] - 190, 50), CLOUD_SIZE))
    pygame.draw.ellipse(dis, WHITE, ((int(SIZE[0] / 2), 10), CLOUD_SIZE))
    pygame.draw.ellipse(dis, WHITE, ((int(SIZE[0] / 2), 60), CLOUD_SIZE))
    pygame.draw.ellipse(dis, WHITE, ((-int(CLOUD_SIZE[0] / 2), 50), CLOUD_SIZE))
    pygame.draw.ellipse(dis, WHITE, ((-int(CLOUD_SIZE[0] / 2) - 20, 20), CLOUD_SIZE))

    pygame.draw.circle(dis, RED, (int(SIZE[0] / 2), int(SIZE[1] / 2) - aux_right), BALOON_SIZE)
    pygame.draw.rect(dis, BROWN, ((BASKET_COORDINATES[0], BASKET_COORDINATES[1] - aux_right), BASKET_SIZE))

    pygame.draw.arc(dis, BROWN, (int(SIZE[0] / 2 - BALOON_SIZE), int(SIZE[1] / 2 - 15 - aux_right),
                                 2 * BALOON_SIZE, 30), pi, 2 * pi, 5)
    pygame.draw.arc(dis, BROWN, (int(SIZE[0] / 2 - BALOON_SIZE), int(SIZE[1] / 2 - BALOON_SIZE) - aux_right,
                                 2 * BALOON_SIZE, BASKET_COORDINATES[1] + BALOON_SIZE + int(BASKET_SIZE[1] * 0.6)
                                 - int(SIZE[1] / 2)), pi / 2, 3 * pi / 2, 5)
    pygame.draw.arc(dis, BROWN, (int(SIZE[0] / 2 - BALOON_SIZE), int(SIZE[1] / 2 - BALOON_SIZE) - aux_right,
                                 2 * BALOON_SIZE, BASKET_COORDINATES[1] + BALOON_SIZE + int(BASKET_SIZE[1] * 0.6)
                                 - int(SIZE[1] / 2)), 3 * pi / 2, 5 * pi / 2, 5)
    pygame.draw.arc(dis, BROWN, (int(SIZE[0] / 2 - BALOON_SIZE / 2), int(SIZE[1] / 2 - BALOON_SIZE) - aux_right,
                                 BALOON_SIZE, BASKET_COORDINATES[1] + BALOON_SIZE + int(BASKET_SIZE[1] / 3)
                                 - int(SIZE[1] / 2)), pi / 2, 3 * pi / 2, 5)
    pygame.draw.arc(dis, BROWN, (int(SIZE[0] / 2 - BALOON_SIZE / 2), int(SIZE[1] / 2 - BALOON_SIZE) - aux_right,
                                 BALOON_SIZE, BASKET_COORDINATES[1] + BALOON_SIZE + int(BASKET_SIZE[1] / 3)
                                 - int(SIZE[1] / 2)), 3 * pi / 2, 5 * pi / 2, 5)

    pygame.time.Clock().tick(60)
    pygame.display.update()
    if SIZE[0] - aux_left + BALOON_SIZE*2 <= 0:
        aux_left = -int(BALOON_SIZE*1.8)
    if SIZE[1] - aux_right - BASKET_SIZE[1] <= 0:
        aux_right = -int(SIZE[1]/2) - BALOON_SIZE