import pygame
import random
from pygame.locals import *


class Rain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rain_img
        self.rect = self.image.get_rect()
        self.speedx = 3
        self.speedy = random.randint(0, 25)
        self.rect.x = random.randint(10, wn_width)
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
rain_img = pygame.image.load("images/money.png")

#setup window
wn_width = 800
wn_height = 600
wn = pygame.display.set_mode((wn_width, wn_height))
pygame.display.set_caption("Coins Rain")

#Create sprite group
rain_group = pygame.sprite.Group()

for i in range(200):
    rain = Rain()
    rain_group.add(rain)

#scores
scores = 0
font = pygame.font.SysFont("monospace", 32)
mask=pygame.Surface((180,100),pygame.SRCALPHA)
textX = 750
textY = 550

def show_score(x, y):
    score = font.render("Score: " + str(scores), True, (0, 255, 0))
    wn.blit(score, (x, y), special_flags=(pygame.BLEND_RGBA_ADD))
    



#Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            scores += 1
            
            print(f"Scores: {scores}")
            

        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #update
    show_score(textX, textY)
    rain_group.update()
    
    wn.fill(WHITE)
    rain_group.draw(wn)
    pygame.display.flip()
    clock.tick(20)

#QUIT
pygame.quit()
quit()