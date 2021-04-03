import pygame
import random

pygame.init()

black = (0, 0 , 0)
white = (255, 255, 255)

myDisplay = pygame.display.set_mode((1110, 600))
pygame.display.set_caption("Farm House")

SnowFlakes = []

#---------------------------------------------------------------------------------------------------------------------------------------------------------

for q in range(100):
    x = random.randrange(0, 1110)
    y = random.randrange(0, 590)
    SnowFlakes.append([x, y])

#.........................................................................................................................................................

clock = pygame.time.Clock()
farm = False
background_position = [0, 0]

background_image = pygame.image.load("farm3.jpeg").convert() #https://yputube.com/PneE00FdCdw
while not farm:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            farm = True

    myDisplay.blit(background_image, background_position)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

for i in SnowFlakes:
    i[1] += 1
    pygame.draw.circle(myDisplay, white, i, 7)

    if i[1] > 580:

        i[1] = random.randrange(-50, -5)
        i[0] = random.randrange(1110)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.display.flip()
    clock.tick(60)
pygame.quit()