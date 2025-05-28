import pygame
from constants import *
from player import Player
def main():
    # create groups for organization
    # should assign groups before creating object
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    print("Starting Asteroids!")
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)



    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for asset in drawable:
            asset.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000  # dt based on refresh rate or fps i guess


if __name__ == "__main__":
    main()
