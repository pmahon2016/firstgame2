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

#variables to track image
xpos = 100
ypos = 500

while True:  # continious loop
    # fill the window background color
    MY_DISPLAY.fill(black)
    # put "dog" image on windows at the x and y coordinates
    MY_DISPLAY.blit(dog, (xpos, ypos))

    for event in pygame.event.get():  # poll for new events such as mouse clicks or key press

        if event.type == pygame.QUIT:  # if the user quits (clicks the X on the window)
            pygame.quit()  # we quit our program
            sys.exit() #  *** exit the game
        # new even to check for key press by user

        elif event.type ==pygame.KEYDOWN:

        # if key up or down move image accordingly
            if event.key == pygame.K_UP:
                ypos -=10
            elif event.key == pygame.K_DOWN:
                ypos +=10
            elif event.key == pygame.K_RIGHT: # added right key movement
                xpos += 10

            elif event.key == pygame.K_LEFT: # added left key movement
                xpos -= 10


        pygame.display.flip()  # constantly refreshing the screen
