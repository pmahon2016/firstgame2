import pygame

image = pygame.image.load("drone.png")

rect = image.get_rect()

def load_image(screen):

    screen_rect = screen.get_rect()

    # rect.centerx = screen_rect.centerx
    rect.right = screen_rect.right
    # rect.bottom = screen_rect.bottom
    rect.top = screen_rect.top
    direction = 'left'


