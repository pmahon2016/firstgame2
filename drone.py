import pygame


class Drone:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("drone.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.top = self.screen_rect.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)
