import pygame
import drone



def check_events():
    direction = "left"
    for event in pygame.event.get():
                # check if the event is the X button
                if event.type==pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)

    if direction == 'right':
        drone.rect.centerx += 5
        if drone.rect.centerx > 10:
            direction = 'left'

    elif direction == 'left':
        drone.rect.centerx -= 5
        if drone.rect.left < -50:
            drone.rect.right = drone.screen_rect.right
            drone.rect.top = drone.screen_rect.top
            direction = 'left'

    screen.blit(image, rect)