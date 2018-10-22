import pygame
import game_settings as settings


screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))

image = pygame.image.load("drone.png")

rect = image.get_rect()
screen_rect = screen.get_rect()

# rect.centerx = screen_rect.centerx
rect.right = screen_rect.right
# rect.bottom = screen_rect.bottom
rect.top = screen_rect.top



def blitme():
    direction = 'left'
    screen.fill(settings.bg_color)
    if direction == 'right':
        rect.centerx +=5
        if rect.centerx > 10:
            direction = 'left'

    elif direction == 'left':
        rect.centerx -= 5
        if rect.left < -50:
            rect.right = screen_rect.right
            rect.top = screen_rect.top
            direction = 'left'

    # 6 - draw the screen elements
    screen.blit( image, rect)