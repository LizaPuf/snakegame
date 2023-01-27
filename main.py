import pygame
import sys
import random


SIZE_BLOCK = 20
FRAME_COLOR = (223, 185, 136)
SQUARE_COLOR = (246, 240, 212)
SQUARE_COLOR_2 = (255, 255, 255)
SNAKE_COLOR = (34, 139, 34)
HEADER_COLOR = (200, 160, 110)
COUNT_BLOCKS = 20
MARGIN = 1
HEADER_SIZE = 70
size = [SIZE_BLOCK*COUNT_BLOCKS+2*COUNT_BLOCKS+MARGIN*COUNT_BLOCKS, SIZE_BLOCK*COUNT_BLOCKS+2*COUNT_BLOCKS+MARGIN*COUNT_BLOCKS + HEADER_SIZE]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
timer = pygame.time.Clock()

class SnakeBlocks:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK

snakeblocks = [SnakeBlocks(9, 8), SnakeBlocks(9, 9), SnakeBlocks(9, 10)]
d_col = 1
d_row = 0
def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_SIZE + COUNT_BLOCKS + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row += 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col += 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_SIZE])

    for row in range(COUNT_BLOCKS):

        for column in range(COUNT_BLOCKS):
            if (row+column) % 2 == 0:
                color = SQUARE_COLOR
            else:
                color = SQUARE_COLOR_2
            draw_block(color, row, column)

    head = snakeblocks[-1]
    if not head.is_inside():
        print('crash')
        pygame.quit()
        sys.exit()

    for block in snakeblocks:
        draw_block(SNAKE_COLOR, block.x, block.y)


    new_head = SnakeBlocks(head.x + d_row, head.y + d_col)
    snakeblocks.append(new_head)
    snakeblocks.pop(0)

    pygame.display.flip()
    timer.tick(2)
