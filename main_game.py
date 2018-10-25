import pygame
import loadimages  # import the module to load screen settings and images
import game_controls as gc

gc.direction = 'left'  # set the initial variable to move the drone and boat left or right
gc.boatdir = 'right'
# Initialize the game
pygame.init()

# keep looping through

while True:

    #load the image(s)
    loadimages.blitme(gc.direction, gc.boatdir)  # call the blitme function in loadimages.py to load images
    #clear the screen
    pygame.display.flip() #clear the screen before drawing it again

    # 8 - loop through the key events
    gc.check_events()



