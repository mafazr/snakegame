import pygame
import sys
from settings import *
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.font = pygame.font.SysFont("monospace", 16)

    def update(self):
        if self.snake.move():
            self.game_over()
        
        if self.snake.get_head_position() == self.food.position:
            self.snake.grow()
            self.food.randomize_position()
            # Ensure food doesn't spawn on snake
            while self.food.position in self.snake.positions:
                self.food.randomize_position()

    def draw(self, surface):
        surface.fill(BLACK)
        self.snake.draw(surface)
        self.food.draw(surface)
        
        # Draw Score
        text = self.font.render(f"Score: {self.snake.score}", 1, WHITE)
        surface.blit(text, (5, 10))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snake.turn((0, -1))
            elif event.key == pygame.K_DOWN:
                self.snake.turn((0, 1))
            elif event.key == pygame.K_LEFT:
                self.snake.turn((-1, 0))
            elif event.key == pygame.K_RIGHT:
                self.snake.turn((1, 0))

    def game_over(self):
        self.snake.reset()
