import pygame
import game_controls as gc


class Drone:

    """Simple class to manage the flying drone"""

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(gc.dimage)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.top = self.screen_rect.top


    def blitme(self, direction):
        """ to put (blit) the image on the screen"""


        # to put the drone in perpetual motion on the top of the screen
        if direction == 'right':
            self.rect.centerx += 5
            if self.rect.centerx > 1100:
                gc.direction = 'left'

        elif direction == 'left':
            self.rect.centerx -= 5
            if self.rect.centerx < 100:
                gc.direction = 'right'

        # the drop is call by the user by pressing the down arror. See Game Controls
        # that check the users inputs for the game loop
        elif direction == 'drop':
            self.rect.centery += 5
            gc.direction = 'drop'

            # keeps dropping until the drone gets near the bottom of the screen
            if self.rect.centery > 700:
                temp = abs(gc.boatloc - self.rect.centerx)
                if temp > 100:  # is the drone close enough to the boat?
                    self.image = pygame.image.load('boom.png')
                    crash_sound = pygame.mixer.Sound('splash.wav')
                    pygame.mixer.Sound.play(crash_sound)
                    gc.droneflag = False  # to make the drone disappear. setting switches in Game Controls

                else:
                    self.image = pygame.image.load('safe.png')  # well done image
                    yay = pygame.mixer.Sound('congrats.flac')
                    pygame.mixer.Sound.play(yay)
                    self.rect.centery = 300
                    gc.direction = "nothing"

        self.screen.blit(self.image, self.rect) #put the image on the screen
