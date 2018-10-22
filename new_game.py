# 1 - Import library
import pygame

import game_settings as settings
# 2 - Initialize the game
pygame.init()

screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))



# 3 - Load images and put initial postion at bottom center

image = pygame.image.load("dog.png")

rect = image.get_rect()
screen_rect = screen.get_rect()

rect.centerx = screen_rect.centerx
rect.bottom = screen_rect.bottom

direction = 'right'


# 4 - keep looping through
while True:
    # 5 - clear the screen before drawing it again
    screen.fill(settings.bg_color)
    if direction == 'right':
        rect.centerx +=5
        if rect.centerx > 1100:
            direction = 'up'
    elif direction == 'up':
        rect.top -= 5
        if rect.centery < 50:
            direction = 'left'
    elif direction == 'left':
        rect.centerx -= 5
        if rect.left < 100:
            direction = 'down'
    elif direction == 'down' :
        rect.centery += 5
        if rect.centery >700:
            direction = 'right'

    # 6 - draw the screen elements
    screen.blit( image, rect)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)


