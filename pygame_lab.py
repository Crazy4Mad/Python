import pygame
from math import pi

RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (225, 225, 0)
BROWN = (150, 75, 0)
STRONG_BLUE = (0, 0, 100)
SIZE = (500, 400)
BALLOON_SIZE = 60
CLOUD_SIZE = (150, 90)
SUN_SIZE = 100
K = 0.8
BASKET_COORDINATES = (int(SIZE[0]/2)-K*BALLOON_SIZE, int(SIZE[1]/2)+1.5*K*BALLOON_SIZE)
BASKET_SIZE = (BALLOON_SIZE*2*K, 50)

pygame.init()
dis = pygame.display.set_mode(SIZE)

dis.fill(STRONG_BLUE)
pygame.draw.circle(dis, YELLOW, (SIZE[0], int(SUN_SIZE*0.8)), SUN_SIZE)
pygame.draw.ellipse(dis, WHITE, ((200, 40), CLOUD_SIZE))
pygame.draw.ellipse(dis, WHITE, ((SIZE[0] - 190, 50), CLOUD_SIZE))
pygame.draw.ellipse(dis, WHITE, ((int(SIZE[0] / 2), 10), CLOUD_SIZE))
pygame.draw.ellipse(dis, WHITE, ((int(SIZE[0] / 2), 60), CLOUD_SIZE))
pygame.draw.ellipse(dis, WHITE, ((-int(CLOUD_SIZE[0]/2), 50), CLOUD_SIZE))
pygame.draw.ellipse(dis, WHITE, ((-int(CLOUD_SIZE[0]/2) - 20, 20), CLOUD_SIZE))

pygame.draw.circle(dis, RED, (int(SIZE[0] / 2), int(SIZE[1] / 2)), BALLOON_SIZE)
pygame.draw.rect(dis, BROWN, (BASKET_COORDINATES, BASKET_SIZE))

pygame.draw.arc(dis, BROWN, (int(SIZE[0]/2 - BALLOON_SIZE), int(SIZE[1]/2 - 15), 2*BALLOON_SIZE, 30),
                pi, 2*pi, 5)
pygame.draw.arc(dis, BROWN, (int(SIZE[0]/2 - BALLOON_SIZE), int(SIZE[1]/2 - BALLOON_SIZE),
                             2*BALLOON_SIZE, BASKET_COORDINATES[1] + BALLOON_SIZE + int(BASKET_SIZE[1]*0.6)
                             - int(SIZE[1] / 2)), pi/2, 3*pi/2, 5)

pygame.draw.arc(dis, BROWN, (int(SIZE[0]/2 - BALLOON_SIZE), int(SIZE[1]/2 - BALLOON_SIZE),
                             2*BALLOON_SIZE, BASKET_COORDINATES[1] + BALLOON_SIZE + int(BASKET_SIZE[1]*0.6)
                             - int(SIZE[1] / 2)), 3*pi/2, 5*pi/2, 5)

pygame.draw.arc(dis, BROWN, (int(SIZE[0]/2 - BALLOON_SIZE/2), int(SIZE[1]/2 - BALLOON_SIZE),
                             BALLOON_SIZE, BASKET_COORDINATES[1] + BALLOON_SIZE + int(BASKET_SIZE[1]/3)
                             - int(SIZE[1] / 2)), pi/2, 3*pi/2, 5)

pygame.draw.arc(dis, BROWN, (int(SIZE[0]/2 - BALLOON_SIZE/2), int(SIZE[1]/2 - BALLOON_SIZE),
                             BALLOON_SIZE, BASKET_COORDINATES[1] + BALLOON_SIZE + int(BASKET_SIZE[1]/3)
                             - int(SIZE[1] / 2)), 3*pi/2, 5*pi/2, 5)
pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    pygame.time.Clock().tick(60)
    pygame.display.update()