import pygame
import random
import math

pygame.init() #Iniatie pygame

FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (110, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20 #Velocity the squares will move with -> 20 pixels per second

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Py2048")


def main(window): #defines the game loop and event for quitting
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()


if __name__ == "__main__": 
    main(WINDOW)
