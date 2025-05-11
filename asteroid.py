import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.score_value = self._determine_score_value()
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position +=(self.velocity * dt)

    def _determine_score_value(self):
        if self.radius==ASTEROID_MIN_RADIUS:
            return ASTEROID_MIN_VALUE
        elif self.radius==ASTEROID_MIN_RADIUS*2:
            return ASTEROID_MED_VALUE
        elif self.radius==ASTEROID_MIN_RADIUS*3:
            return ASTEROID_MAX_VALUE

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        A1=Asteroid(self.position.x,self.position.y,(self.radius-ASTEROID_MIN_RADIUS))
        A2=Asteroid(self.position.x,self.position.y,(self.radius-ASTEROID_MIN_RADIUS))

        A1.velocity=pygame.math.Vector2.rotate(self.velocity,angle) * 1.2
        A2.velocity=pygame.math.Vector2.rotate(self.velocity,-angle) * 1.2
    
    


       
