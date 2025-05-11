import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from renderer import Renderer
from explosion import Explosion
import random
import math
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosion_group = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Explosion.containers = (explosion_group, updatable, drawable)
    renderer = Renderer(screen)

    with open("statics/high score.txt",'r') as f:
            high_score=f.read()
    dt = 0
    user_lost_live = False

    while True:
        player_collided_this_frame = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE) or (event.type == pygame.QUIT):
                    return
        
        updatable.update(dt)



        for id1, asteroid1 in enumerate(asteroids):
            if player.collides_with(asteroid1):
                player.lost_live()
                break
            
            
            for shot in shots:
                if asteroid1.collides_with(shot):
                    player.successful_shot(asteroid1)
                    explosion = Explosion(asteroid1.position.x,asteroid1.position.y)
                    explosion_group.add(explosion)
                    asteroid1.split()
                    shot.kill()
        



                    
                


            

        screen.fill("black")
        
        renderer.draw_score(player.score,high_score)

        for i in range(1,player.lives+1):
            renderer.draw_heart((SCREEN_WIDTH + (HEART_PADDING_x + (HEART_PADDING_x/2) * i)-350,SCREEN_HEIGHT + HEART_PADDING_y))


        for obj in drawable:
            obj.draw(screen)

        explosion_group.draw(screen)
        explosion_group.update()
        

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()
