import pygame

def check_events():
    direction = "left"
    for event in pygame.event.get():
                # check if the event is the X button
                if event.type==pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)

