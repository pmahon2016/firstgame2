import pygame
import game_controls as gc




class Boat:
    """Class to manage the boat"""

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("boat1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.right = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self, boatdir):

        """to move the boat continuously from left to right"""

        if boatdir == 'right':
            self.rect.centerx += 1
            gc.boatloc = self.rect.centerx  # record the location of boat to see if the drone lands near
            if self.rect.centerx > 1000:
                gc.boatdir = 'left'

        if boatdir == 'left':
            self.rect.centerx -= 1
            gc.boatloc = self.rect.centerx # record the location of boat to see if the drone lands near
            if self.rect.centerx < 100:
                gc.boatdir = 'right'

        self.screen.blit(self.image, self.rect)
