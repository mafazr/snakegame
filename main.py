import pygame
import sys
from settings import *
from game import Game

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game.handle_input(event)

        game.update()
        game.draw(screen)
        
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
