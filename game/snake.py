import pygame
from .setting import BLACK

class Snake:
    def __init__(self):
        self.body = [[300, 200]]
        self.direction = [0, 0]

    def Move(self):
        """
        Head direction
        """
        head = [self.body[-1][0] + self.direction[0], self.body[-1][1] + self.direction[1]]
        self.body.append(head)

    def Grow(self):
        """
        Increase the size of the snake
        """
        pass

    def CheckCollision(self):
        """
        Check if the snake collides with the screen
        """
        head = self.body[-1]
        return head in self.body[:-1]
    
    def Draw(self, screen, block_size):
        """
        Draw the snake
        """
        for block in self.body:
            pygame.draw.rect(screen, BLACK, (block[0], block[1], block_size, block_size))