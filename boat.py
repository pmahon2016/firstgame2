import pygame


class Boat:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("boat1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.right = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom



    def blitme(self):
        self.screen.blit(self.image, self.rect)