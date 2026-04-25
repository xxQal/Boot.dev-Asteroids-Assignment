import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_direction = random.uniform(20, 50)
            split1 = self.velocity.rotate(new_direction)
            split2 = self.velocity.rotate(-new_direction)
            new_radius = (self.radius - ASTEROID_MIN_RADIUS)
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = (split1 * 1.2)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = (split2 * 1.2)
