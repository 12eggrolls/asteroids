import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
def main():
    # create groups for organization
    # should assign groups before creating object
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    print("Starting Asteroids!")
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for asset in drawable:
            asset.draw(screen)
        
        for asteroid in asteroids:
            if player.is_collided(asteroid):
                print("Game over!")
                sys.exit(0)
        
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.is_collided(asteroid):
                    asteroid.kill()
                    bullet.kill()

        pygame.display.flip()
        dt = clock.tick(60)/1000  # dt based on refresh rate or fps i guess


if __name__ == "__main__":
    main()
