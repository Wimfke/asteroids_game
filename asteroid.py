import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            2)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            self.spawn(radius, self.position, velocity1 * 1.2)
            self.spawn(radius, self.position, velocity2 * 1.2)