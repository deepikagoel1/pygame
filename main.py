import pygame

#initialise pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Coin Invaders")
icon = pygame.image.load("money.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('big.png')
playerX = 370
playerY = 10

def player():
    screen.blit(playerImg, (playerX, playerY))

#Game Loop
running = True
while running:
    #RGB --> Red, Green, Blue
    screen.fill((0, 0 , 0));
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    
    player()
    pygame.display.update() #Updating the screen color
