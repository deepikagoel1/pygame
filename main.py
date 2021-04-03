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
#playerY = 480
playerY = 10

#code had beed drawn on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))

#Game Loop
running = True
while running:
    #RGB --> Red, Green, Blue
    screen.fill((0, 0 , 0));
    #playerY += 0.1 #movement from top to bottom
    #playerX += 0.1 #movement in right direction
    #playerX -= 0.1 #movement in left direction
    #playerY -= 0.1 #movement from bottom to top
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    #if keystroke is pressed checked whether it is top or bottom
        if event.type ==pygame.KEYDOWN:
            print("A Keystroke is pressed")
            if event.key == pygame.K_LEFT:
                print("LEFT arrow key is pressed")
            if event.key == pygame.K_RIGHT:
                print("RIGHT arrow key is pressed")

        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been pressed")

    player(playerX, playerY)
    pygame.display.update() #Updating the screen color
