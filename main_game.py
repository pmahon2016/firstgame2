import pygame
import drone
import game_controls as gc

# Initialize the game
pygame.init()


# keep looping through
while True:
    # 5 - clear the screen before drawing it again
    drone.blitme()
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    gc.check_events()



