import pygame
from settings import *

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = (0, 0) # Initially stationary
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        
        # Check for self collision (excluding head which is not in positions yet for the check effectively, 
        # but actually we check against existing positions)
        if len(self.positions) > 2 and new in self.positions[2:]:
             return True # Collision detected

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        
        return False # No collision

    def grow(self):
        self.length += 1
        self.score += 1

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, GREEN, r)
            pygame.draw.rect(surface, BLACK, r, 1) # Border
