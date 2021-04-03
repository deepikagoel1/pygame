import pygame
import sys
import time

black = (0, 0, 0)
white = (255, 255, 255)
cool_blue = (30, 144, 255)
cooler_blue = (30, 175, 255)
display_width = 1000
display_height = 500

pygame.init()
game_screen = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption('Clicker')
clock = pygame.time.Clock()
max_fps = 15

def txt_obj(text, font):
    """Creates object for text to be created on"""
    Text_Surface = font.render(text, True, black)
    return Text_Surface, Text_Surface.get_rect()

# def display_messages(text, xr, yr):
#     cool_titletext = pygame.Font.font('Quicksand-Regular.ttf', 50)
#     txt_surface, txt_rect = txt_obj(text, cool_titletext)
#     txt_rect.center = (display_width*xr, display_height*yr)
#     game_screen.blit(txt_surface, txt_rect)
#     pygame.display.update()



def startButton(x, y, width, height, old_color, new_color):
    """Used for the start button, enters the game"""
    mouse = pygame.mouse.get_pos()
    pygame.draw.rect(game_screen, old_color,(x, y, width, height))
    if x + width > mouse[0] > x and  y + height > mouse[1] > y:
        pygame.draw.rect(game_screen, new_color, (x, y , width, height))
    else:
        pygame.draw.rect(game_screen, old_color,(x, y, width, height))

def anyOtherButton(x, y, width, height, old_color, new_color):
    """Will be used for any other button other than the start button."""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(game_screen, old_color,(x, y, width, height))
    if x + width > mouse[0] > x and  y + height > mouse[1] > y:
        pygame.draw.rect(game_screen, new_color, (x, y , width, height))
        if click != None and click[0] == 1:
            print("i need to figure this one out lol")
    else:
        pygame.draw.rect(game_screen, old_color,(x, y, width, height))


def game_intro():
    """Main menu screen"""
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                break
                
        game_screen.fill(white)
        cool_titletext = pygame.font.Font("Quicksand-Regular.ttf", 50)
        txt_surface, txt_rect = txt_obj("Welcome to Productivity Clicker", cool_titletext)
        txt_rect.center = ((display_width/2), (display_height/2))
        game_screen.blit(txt_surface, txt_rect)
        
        start_button = startButton
        start_button(400, 300, 250, 50, cool_blue, cooler_blue)
        button_text = pygame.font.Font("Quicksand-Regular.ttf",30)
        txt_surface, txt_rect = txt_obj("Start", button_text)
        txt_rect.center = ((400+(250/2)), (300+(50/2)))
        game_screen.blit(txt_surface, txt_rect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 400 + 250 > mouse[0] > 400 and  300 + 50 > mouse[1] > 300:
            if click != None and click[0] == 1:
                print("hi")
                game_screen.fill(white)
                pygame.display.update()
                break
                # start_game()
                # done = True
                # return None
            

        pygame.display.update()
        clock.tick(max_fps)


# class Status:
#     def __init__(self, productivity, increment):
#         self.productivity = productivity
#         self.increment = increment
#         self.start_time = time.time()
    
#     def is_clicked(self):
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:

def start_game():
    """Running game, WIP"""
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                break
        
                

        anyOtherButton(200, 300, 250, 50, cool_blue, cooler_blue)
        button_text = pygame.font.Font("Quicksand-Regular.ttf", 15)
        txt_surface, txt_rect = txt_obj("Click to increase productivity!", button_text)
        txt_rect.center = ((200+(250/2)), (300+(50/2)))
        game_screen.blit(txt_surface, txt_rect)
        pygame.display.update()
        clock.tick(max_fps)
        
game_intro()
start_game()
pygame.quit()