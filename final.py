import pygame
import random
from pygame.locals import *


width = 800
height = 600

score = 0
#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


#initialize Pygame and create window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME DEVELOPED BY DEEPIKA !!")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface =font.render("Score: " + str(score), True, BLUE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
#class definition

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/money.png")
        self.rect = self.image.get_rect()
        self.speedx = 1
        self.speedy = random.randint(0, 25)
        self.rect.x = random.randint(10, width)
        self.rect.y = random.randint(-height, -5)
        self.radius = int(self.rect.width * .85 /2)

    def update(self):
    
        if self.rect.bottom > height:
            self.speedx = 1
            self.speedy = random.randint(5, 25)
            self.rect.x = random.randint(-width, width)
            self.rect.y = random.randint(-height, -5)
        self.rect.x += self.speedx
        self.rect.y += self.speedy


#all_sprites = pygame.sprite.Group()
#Create sprite group
game_group = pygame.sprite.Group()
for i in range(200):
    game = Game()
    game_group.add(game)

#Game Loop
while True:
    #process input (events)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            score += 1
            print(f"Scores: {score}")
        #check for closing window
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #Update
    game_group.update()

    #Draw/Render

    screen.fill(WHITE)
    game_group.draw(screen)
    draw_text(screen, str(score), 32, width /2, 10)

    # *after* drawing everything, flip the display
    pygame.display.flip()
    clock.tick(20)
    
pygame.quit()
quit()