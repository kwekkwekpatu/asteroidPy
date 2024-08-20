import pygame
from constants import *
from asteroid import Asteroid
from asteroidField import AsteroidField
import player as pl

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = pl.Player(x= SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    pl.Player.containers = (updatable, drawable)

    updatable.add(player, asteroid_field)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")
        for element in updatable:
            element.update(dt)

        screen.fill("black")

        for element in drawable:
            element.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
