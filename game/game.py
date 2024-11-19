import pygame
from .setting import *
from .snake import Snake
from .food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_style = pygame.font.SysFont("comicsansms", 35)
        self.snake = Snake()
        self.food = Food()
        self.running = True

    def DisplayScore(self, score):
        value = self.score_style.render(f"Score: {score}", True, GREEN)
        self.screen.blit(value, [10, 10])

    def GameOver(self):
        message = self.font_style.render("Game Over! (Q to Quit and R to Restart)", True, RED)
        self.screen.blit(message, [WIDTH / 6, HEIGHT / 3])
        pygame.display.update()

    def CheckCollision(self):
        head = self.snake.body[-1]
        if head[0] >= WIDTH or head[0] < 0 or head[1] >= HEIGHT or head[1] < 0:
            return True
        return False

    def Run(self):
        while self.running:
            self.HandleEvents()
            self.UpdateGame()
            self.RenderGame()
            self.clock.tick(SNAKE_SPEED)
        pygame.quit()

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.snake.direction != [10, 0]:
                    self.snake.direction = [-10, 0]
                elif event.key == pygame.K_RIGHT and self.snake.direction != [-10, 0]:
                    self.snake.direction = [10, 0]
                elif event.key == pygame.K_UP and self.snake.direction != [0, 10]:
                    self.snake.direction = [0, -10]
                elif event.key == pygame.K_DOWN and self.snake.direction != [0, -10]:
                    self.snake.direction = [0, 10]

    def UpdateGame(self):
        self.snake.Move()
        if self.snake.body[-1] == self.food.position:
            self.snake.Grow()
            self.food.position = self.food.GeneratePosition()
        else:
            self.snake.body.pop(0)
        if self.CheckCollision() or self.snake.CheckCollision():
            self.running = False

    def RenderGame(self):
        self.screen.fill(WHITE)
        self.food.Draw(self.screen)
        self.snake.Draw(self.screen, SNAKE_BLOCK)
        self.DisplayScore(len(self.snake.body) - 1)
        pygame.display.update()