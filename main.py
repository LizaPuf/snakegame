import pygame
import random
SIZE_BLOCK = 20
FRAME_COLOR = (223, 185, 136)
SQUARE_COLOR = (246, 240, 212)
SQUARE_COLOR_2 = (255, 255, 255)
COUNT_BLOCKS = 20
MARGIN = 1
size = [500, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)

    for row in range(COUNT_BLOCKS):

        for column in range(COUNT_BLOCKS):
            if (row+column) % 2 == 0:
                color = SQUARE_COLOR
            else:
                color = SQUARE_COLOR_2
            pygame.draw.rect(screen, color, [10+column*SIZE_BLOCK+MARGIN*(column+1),
                                             20+row*SIZE_BLOCK+MARGIN*(row+1),
                                             SIZE_BLOCK,
                                             SIZE_BLOCK])
    pygame.display.flip()
