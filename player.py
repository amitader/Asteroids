import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
import sys


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.score=0
        self.lives=PLAYER_MAX_LIVES
        self.invulnerable=False
        self.invulnerable_timer=0
        self.is_visible=True
    def draw(self, screen):
        if self.is_visible:
            pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        if self.invulnerable:
            if self.is_visible:
                self.is_visible=False
            else:
                self.is_visible=True
            self.invulnerable_timer -= dt
            if self.invulnerable_timer <= 0:
                self.invulnerable = False
                self.is_visible=True
        
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()


    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def successful_shot(self,asteroid):
        self.score+=asteroid.score_value
        #print(f"shot an asteroid with a radious: {asteroid.radius} and a value: {asteroid.score_value}, now the score is: {self.score}" )
    
    
    def lost_live(self):
        if not self.invulnerable:
            self.lives-=1
            self.invulnerable = True
            self.invulnerable_timer = 2.0
            if self.lives<=0:
                    print("Game over!")
                    print(f"Player score: {self.score}")
                    with open("statics/high score.txt",'r') as f:
                        old_score=int(f.read().strip())
                    if old_score<self.score:
                        with open("statics/high score.txt",'w') as f:
                                f.write(str(self.score))
                    
                    sys.exit()
       

