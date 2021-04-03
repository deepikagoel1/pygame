import pygame
import random
from pygame.locals import *


pygame.init()

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

myDisplay = pygame.display.set_mode((800, 600))

coins = []

#---------------------------------------------------------------------------------------------------------------------------------------------------------

for q in range(100):
    x = random.randrange(0, 800)
    y = random.randrange(0, 590)
    coins.append([x, y])

#.........................................................................................................................................................

clock = pygame.time.Clock()
farm = False
background_position = [0, 0]

background_image = pygame.image.load("images/money.png")
while not farm:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            farm = True

    myDisplay.blit(background_image, background_position)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

for i in coins:
    i[1] += 1
    background_image = pygame.image.load("images/money.png")

    if i[1] > 580:

        i[1] = random.randrange(-50, -5)
        i[0] = random.randrange(1110)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.display.flip()
    clock.tick(60)
pygame.quit()