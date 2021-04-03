import pygame
import random
#initialise pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Coin Invaders")
icon = pygame.image.load("images/money.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('images/money.png')
#playerX = 370
#playerY = 480
playerY = 10
playerX = random.randint(0, 600)
playerY = random.randint(10, 100)
playerY_change = 0

#coins
coinsX = random.randint(0, 600)
coinsY = random.randint(10, 100)
coinsY_change = 0
coinsImg = pygame.image.load('images/dollar.png')

#code had beed drawn on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))

def dollar(x, y):
    screen.blit(coinsImg, (x, y))

#Create sprite group
coinImg = pygame.sprite.Group()

#Game Loop
running = True
while running:
    #RGB --> Red, Green, Blue
    screen.fill((0, 0 , 0));
    playerY += 0.1 #movement from top to bottom
    #playerX += 0.1 #movement in right direction
    #playerX -= 0.1 #movement in left direction
    #playerY -= 0.1 #movement from bottom to top
    coinsY += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    '''
    #if keystroke is pressed checked whether it is top or bottom
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1
            if event.key == pygame.K_UP:
                playerY_change = -0.1

        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    '''

    #playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 566:    #set the boundary as Y axis = 600 and image size selected as 64 so 600-34 = 536 and X-axis set to 800 so 800-64 = 
        playerY = 566

    #Dollars
    if coinsY <= 0:
        coinsY = 0
    elif coinsY >= 566:    #set the boundary as Y axis = 600 and image size selected as 64 so 600-34 = 536 and X-axis set to 800 so 800-64 = 
        coinsY = 566


    player(playerX, playerY)
    dollar(coinsX, coinsY)
    pygame.display.update() #Updating the screen color
