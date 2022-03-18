import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_SIZE = 800

def main():
    global SCREEN, CLOCK, nrArr
    nrArr = list(range(1, 101))
    random.shuffle(nrArr)
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('SETKA GAME')
    icon = pygame.image.load('100.png')
    pygame.display.set_icon(icon)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            SCREEN.fill(WHITE)
            drawGrid()
        pygame.display.update()
        CLOCK.tick(30)


def drawGrid():
    blockSize = int(WINDOW_SIZE/10) #Set the size of the grid block\
    i = 0
    for y in range(0, WINDOW_SIZE, blockSize):
        for x in range(0, WINDOW_SIZE, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
            text = pygame.font.SysFont('Arial',35).render(str(nrArr[i]), True, BLACK)
            SCREEN.blit(text, (x + blockSize/3, y + blockSize/3))
            i += 1


main()