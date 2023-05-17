import pygame, sys
from settings import *
from window import Window


class Main:  # Main class
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))   #
        self.clock = pygame.time.Clock()

        self.window = Window()  # Init the editor of the game

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            self.window.run(dt)    # Run the window of the game
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()