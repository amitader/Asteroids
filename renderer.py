import pygame
from constants import *
class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(TEXT_FONT, 30)

    def draw_score(self, score,high_score):
        
        score_text = self.font.render(f"High Score: {high_score} Current Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (SCREEN_WIDTH -450, SCREEN_HEIGHT)) 

    def draw_heart(self,position):
        img = pygame.image.load('sprites/heart pixel art 32x32.png').convert_alpha()
        self.screen.blit(img,position)

    

