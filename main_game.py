import pygame
import game_controls as gc
from drone import Drone
from boat import Boat
import game_settings as settings

gc.direction = 'left'
gc.droneflag = True
gc.boatdir = 'left'

# Initialize the game
pygame.init()

screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
bg = pygame.image.load('sea.jpg')

# keep looping through

drone = Drone(screen)
boat = Boat(screen)

# game loop

while True:

    screen.blit(bg, (0, 0))
    if gc.droneflag:
        drone.blitme(gc.direction)
    boat.blitme(gc.boatdir)
    #clear the screen
    pygame.display.flip() #clear the screen before drawing it again

    # 8 - loop through the key events
    gc.check_events(drone)



