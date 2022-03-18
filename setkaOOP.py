import pygame
import sys
import random


class Screen:

    def __init__(self, size, caption, img):
        self.size = size
        self.screen = pygame.display.set_mode((size, size))
        self.btnlist = []
        self.clicked = []
        for i in range(101):
            self.clicked.append(False)
        pygame.display.set_caption(caption)
        img = pygame.image.load(img)
        pygame.display.set_icon(img)

    def fill(self, col):
        self.screen.fill(col)

    def blit(self, text):
        self.screen.blit(pygame.font.SysFont('Arial', 20).render(str(text), True, (0, 0, 0)), (10, 10))

    def build(self, nrArr):
        blockSize = int(self.size / 10)  # Set the size of the grid block
        i = 0
        for y in range(0, self.size, blockSize):
            for x in range(0, self.size, blockSize):
                name = "btn" + str(nrArr[i])
                name = Button(nrArr[i], x, y, blockSize, self.clicked[i])
                self.btnlist.append(name)
                name.draw(self.screen)
                i += 1


class Button:
    def __init__(self, nr, posX, posY, blockSize, clicked):
        self.nr = nr
        self.posX = posX
        self.posY = posY
        self.blockSize = blockSize
        self.clicked = clicked

    def draw(self, screen):
        self.rect = pygame.Rect(self.posX, self.posY, self.blockSize, self.blockSize)
        colRect = pygame.Rect(self.posX + 1, self.posY + 1, self.blockSize - 2, self.blockSize - 2)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)
        if self.clicked:
            pygame.Surface.fill(screen, (172, 172, 172), rect=colRect)
        screen.blit(pygame.font.SysFont('Arial', 35).render(str(self.nr), True, (0, 0, 0)), (self.posX +
                                                                                             self.blockSize / 3,
                                                                                             self.posY + self.blockSize / 3))

    def click(self):
        if not self.clicked:
            self.clicked = True


class Start:
    def __init__(self, screen):
        self.btnlist = screen.btnlist
        self.clicked = screen.clicked

    def start(screen, nrArr):
        CLOCK = pygame.time.Clock()
        start_ticks = pygame.time.get_ticks()
        while True:
            pygame.display.flip()
            seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    i = -1
                    for btn in screen.btnlist:
                        i += 1
                        if btn.posX < x < btn.posX + btn.blockSize:
                            if btn.posY < y < btn.posY + btn.blockSize:
                                if btn.nr == 1:
                                    btn.click()
                                    screen.clicked[i] = True
                                    break
                                for btnbfr in screen.btnlist:
                                    if btnbfr.nr == btn.nr - 1:
                                        if btnbfr.clicked:
                                            btn.click()
                                            screen.clicked[i] = True
                                            if btn.nr == 100:
                                                if seconds - (seconds // 60 * 60) < 10:
                                                    print("0" + str(seconds // 60) + ":0" + str(
                                                        seconds - (seconds // 60 * 60)))
                                                else:
                                                    print("0" + str(seconds // 60) + ":" + str(
                                                        seconds - (seconds // 60 * 60)))
                                                pygame.quit()
                                                sys.exit()

                                            break
                                        else:
                                            break
                                break
            screen.fill((255, 255, 255))
            screen.build(nrArr)
            if seconds - (seconds // 60 * 60) < 10:
                time = "0" + str(seconds // 60) + ":0" + str(seconds - (seconds // 60 * 60))
            else:
                time = "0" + str(seconds // 60) + ":" + str(seconds - (seconds // 60 * 60))
            screen.blit(time)
            pygame.display.update()
            CLOCK.tick(60)


if __name__ == '__main__':
    nrArr = list(range(1, 101))
    random.shuffle(nrArr)
    pygame.init()
    screen = Screen(800, 'SETKA GAME', "100.png")
    Start.start(screen, nrArr)
