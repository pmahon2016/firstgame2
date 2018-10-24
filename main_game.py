import pygame
import loadimages
import game_controls as gc

gc.direction = 'left'
gc.boatdir = 'right'
# Initialize the game
pygame.init()

# keep looping through


while True:

    #load the image(s)
    loadimages.blitme(gc.direction, gc.boatdir)
    #clear the screen
    pygame.display.flip() #clear the screen before drawing it again

    # 8 - loop through the key events
    gc.check_events()



