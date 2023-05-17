import pygame, sys
from pygame.math import Vector2 as Vector
from pygame.mouse import get_pos as mouse_position
from pygame.image import load
from settings import *


class Window:
    def __init__(self):
        # Main setup
        self.display_surface = pygame.display.get_surface()

        # Navigation
        self.origin = Vector()  # origin point of the current window
        self.mouse_clicked = False
        self.offset = Vector(0, 0)  # Movement value in the 2D space

        # Support grid
        self.support_grid_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.support_grid_surface.set_colorkey("green")
        self.support_grid_surface.set_alpha(30)

    # Event loop
    def event_loop(self):
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game
                pygame.quit()
                sys.exit()
            self.process_input(event)   # Process the inputs of the user

    # Input process (movement,...)
    def process_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:  # Movement started
            self.mouse_clicked = True
            self.offset = Vector(mouse_position()) - self.origin
        if not pygame.mouse.get_pressed()[0]:  # Movement ended
            self.mouse_clicked = False

        # Movement update
        if self.mouse_clicked:
            self.origin = Vector(mouse_position()) - self.offset

        # Scrooling option
        if event.type == pygame.MOUSEWHEEL:
            if pygame.key.get_pressed()[pygame.K_LCTRL]:    # Vertical Scrool
                self.origin.y -= event.y * 50
            else:
                self.origin.x += event.y * 50   # Horizontal Scrool

    # Drawing
    def draw_tiles_grid(self):
        cols = WINDOW_WIDTH // TILE_SIZE
        rows = WINDOW_HEIGHT // TILE_SIZE

        origin_offset = Vector(
            x=self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
            y=self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE
        )

        self.support_grid_surface.fill("green")

        # Draw vertical lines
        for col in range(cols + 1):
            x = origin_offset.x + col * TILE_SIZE
            pygame.draw.line(self.support_grid_surface, LINE_COLOR, (x, 0), (x, WINDOW_HEIGHT))

        # Draw horizontal lines
        for row in range(rows + 1):
            y = origin_offset.y + row * TILE_SIZE
            pygame.draw.line(self.support_grid_surface, LINE_COLOR, (0, y), (WINDOW_WIDTH, y))

        # Display the grid
        self.display_surface.blit(self.support_grid_surface, (0, 0))

    def run(self, dt):
        self.display_surface.fill('white')  # Background color
        self.event_loop()   # Process the events

        # Drawings
        self.draw_tiles_grid()
        pygame.draw.circle(self.display_surface, '#3C3F41', self.origin, 10)

