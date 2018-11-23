import pygame
import game_controls as gc

class Drone:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("drone.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.top = self.screen_rect.top


    def blitme(self,direction):

        if direction == 'right':
            self.rect.centerx += 2
            if self.rect.centerx > 1100:
                gc.direction = 'left'

        elif direction == 'left':
            self.rect.centerx -= 2
            if self.rect.centerx < 100:
                gc.direction = 'right'


        elif direction == 'drop':
            self.rect.centery += 5
            gc.direction = 'drop'
            if self.rect.centery > 600:
                self.remove(self)

        self.screen.blit(self.image, self.rect)
