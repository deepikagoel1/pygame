import pygame
import random
from pygame.locals import *


class Rain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rain_img
        self.rect = self.image.get_rect()
        self.speedx = 3
        self.speedy = random.randint(5, 25)
        self.rect.x = random.randint(-100, wn_width)
        self.rect.y = random.randint(-wn_height, -5)

    def update(self):

        if self.rect.bottom > wn_height:
            self.speedx = 3
            self.speedy = random.randint(5, 25)
            self.rect.x = random.randint(-wn_width, wn_width)
            self.rect.y = random.randint(-wn_height, -5)

        self.rect.x += self.speedx
        self.rect.y += self.speedy

    

pygame.init()

#clock
clock = pygame.time.Clock()

#Define some colors
WHITE = (255, 255, 255)

#images
rain_img = pygame.image.load("images/rain.png")

#setup window
wn_width = 800
wn_height = 600
wn = pygame.display.set_mode((wn_width, wn_height))
pygame.display.set_caption("Torrential Rain")

#Create sprite group
rain_group = pygame.sprite.Group()

for i in range(200):
    rain = Rain()
    rain_group.add(rain)

scores = 0
#Main game loop
while True:
    '''
    # Mouse position and button clicking.
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    # Check if the rect collided with the mouse pos
    # and if the left mouse button was pressed.
    if wn.get_rect().collidepoint(pos) and pressed1:
        #print("You have clicked on rain drop")
        scores += 1
        print(f"Scores: {scores}")
    '''

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #update
    rain_group.update()

    wn.fill(WHITE)
    rain_group.draw(wn)
    pygame.display.flip()
    clock.tick(30)

#QUIT
pygame.quit()
quit()