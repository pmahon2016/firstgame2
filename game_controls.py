import pygame


# # boat and drone move variables. Set in this module to keep state  ( not to be refreshed)
direction = ''
# boatdir = ''

def check_events(ship):

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        elif event.type == pygame.KEYDOWN:

            # if event.key == pygame.K_RIGHT:
            #     li.rectb.centerx +=10
            # # to move the boat manually left and right
            # elif event.key == pygame.K_LEFT:
            #     li.rectb.centerx -= 10

            # make the drone drop
            if event.key == pygame.K_DOWN:
                direction = 'drop'
                ship.blitme(direction)

