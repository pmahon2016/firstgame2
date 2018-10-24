import pygame
import loadimages as li

direction = ''
boatdir = ''

def check_events():

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                li.rectb.centerx +=10

            elif event.key == pygame.K_LEFT:
                li.rectb.centerx -= 10


            elif event.key == pygame.K_DOWN:
                direction = 'drop'
                li.blitme(direction,boatdir)

