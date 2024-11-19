import pygame
import random
from .setting import BLUE, WIDTH, HEIGHT, SNAKE_BLOCK

class Food:
    def __init__(self):
        self.position = self.GeneratePosition()

    def GeneratePosition(self):
        """
        Generate random position for the food
        """
        x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10) * 10
        y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10) * 10
        return [x, y]
    
    def Draw(self, screen):
        """
        Draw the food
        """
        pygame.draw.rect(screen, BLUE, (self.position[0], self.position[1], SNAKE_BLOCK, SNAKE_BLOCK))