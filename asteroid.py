import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        positive_vector = self.velocity.rotate(random_angle)
        negative_vector = self.velocity.rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position
        positive_asteroid = Asteroid(x, y, radius)
        negative_asteroid = Asteroid(x, y, radius)

        positive_asteroid.velocity = positive_vector * 1.2
        negative_asteroid.velocity = negative_vector * 1.2
