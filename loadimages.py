import pygame



# initial loading of screen



# set the rect variable for both the drone and the boat

# boat = pygame.image.load("boat1.png")
#
# rectb = boat.get_rect()



# rect.centerx = screen_rect.centerx

# rectb.left = screen_rect.left
# rectb.centerx = screen_rect.centerx
# rectb.bottom = screen_rect.bottom



# function to move drone  and boat  - called from the game loop
def blitme(direction, boatdir):

    screen.fill(settings.bg_color)
    if direction == 'right':
        rect.centerx +=2
        if rect.centerx > 1100:
            gc.direction = 'left'

    elif direction == 'left':
        rect.centerx -= 2
        if rect.centerx < 100:
            gc.direction = 'right'

    # if the down arror is pressed in Games Settings, drop is set and this loop runs
    elif direction == 'drop':
        rect.centery += 5
        gc.direction = 'drop'

    # boat movement

    if  boatdir == 'right':
        rectb.centerx += 1
        if rectb.centerx > 1000:
            gc.boatdir = 'left'

    if boatdir == 'left':
        rectb.centerx -= 1
        if rectb.centerx < 100:
            gc.boatdir = 'right'


    # 6 - draw three images on the screen. Background, boat and drone after each loop
    # screen.blit(bg, (0, 0))

    # screen.blit(boat, rectb)