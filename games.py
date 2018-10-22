import pygame  # import modules
import sys




pygame.init()  # run pygame

# color variables for some color tuples
green = (0, 255, 0)
red = (255,0,0)
blue = (0,0,255)
white = (255, 255, 255)
black = (0,0,0)

MY_DISPLAY = pygame.display.set_mode((1200, 800))  # send a tuple to the set_mode function for our screen

# ** Create a caption for the display window
pygame.display.set_caption('Hello World!')
#load  the dog.png file
dog = pygame.image.load("dog.png")

rect = dog.get_rect()
screen_rect = MY_DISPLAY.get_rect()

rect.centerx = screen_rect.centerx
rect.bottom = screen_rect.bottom

while True:  # continious loop
    # fill the window background color
    MY_DISPLAY.fill(black)
    # put "dog" image on windows at the x and y coordinates
    MY_DISPLAY.blit(dog, rect)

    for event in pygame.event.get():  # poll for new events such as mouse clicks or key press

        if event.type == pygame.QUIT:  # if the user quits (clicks the X on the window)
            pygame.quit()  # we quit our program
            sys.exit() #  *** exit the game

        # new even to check for key press by user
        elif event.type ==pygame.KEYDOWN:


        # if key up, down, right or left... move image accordingly
            if event.key == pygame.K_UP:
                rect.top -=10
            elif event.key == pygame.K_DOWN:
                rect.bottom +=10
            elif event.key == pygame.K_RIGHT: # added right key movement
                rect.centerx += 10

            elif event.key == pygame.K_LEFT: # added left key movement
                rect.centerx -= 10


        pygame.display.flip()  # constantly refreshing the screen
