import pygame
import game_settings as settings
import game_controls as gc


screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
bg = pygame.image.load('sea.jpg')


image = pygame.image.load("drone.png")
boat = pygame.image.load("boat1.png")
rect = image.get_rect()
rectb = boat.get_rect()
screen_rect = screen.get_rect()


# rect.centerx = screen_rect.centerx
rect.right = screen_rect.right
rectb.left = screen_rect.left
rectb.centerx = screen_rect.centerx
rectb.bottom = screen_rect.bottom
rect.top = screen_rect.top



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

    elif direction == 'drop':
        rect.centery += 5
        gc.direction = 'drop'


    if  boatdir == 'right':
        rectb.centerx += 1
        if rectb.centerx > 1000:
            gc.boatdir = 'left'

    if boatdir == 'left':
        rectb.centerx -= 1
        if rectb.centerx < 100:
            gc.boatdir = 'right'


    # 6 - draw the screen elements
    screen.blit(bg, (0, 0))
    screen.blit( image, rect)
    screen.blit(boat, rectb)