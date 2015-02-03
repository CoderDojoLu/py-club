#!/usr/bin/env python3
import sys, random, pygame, time, os
from pygame.locals import *

WIDTH=640
HEIGHT=480
CELLSIZE=10
assert WIDTH % CELLSIZE == 0, "WIDTH must be a multiple of CELLSIZE"
assert HEIGHT % CELLSIZE == 0, "HEIGHT must be a multiple of CELLSIZE"
CELLWIDTH = WIDTH / CELLSIZE
CELLHEIGHT = HEIGHT / CELLSIZE
x = 100
y = 0
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
os.environ['SDL_VIDEO_CENTERED'] = '1'

# env: SDL_WINDOW_FULLSCREEN - 

BLACK = (0,0,0)
WHITE = (255,255,255)
DARKGRAY = (40,40,40)
GREEN = (0, 255, 0)

def drawGrid():
    for x in range(0, WIDTH, CELLSIZE):
        pygame.draw.line(screen, DARKGRAY, (x,0), (x,HEIGHT))

    for y in range(0, HEIGHT, CELLSIZE):
        pygame.draw.line(screen, DARKGRAY, (0,y), (WIDTH, y))

def blankGrid():
    gridDict = {}
    for y in range(int(CELLHEIGHT)):
        for x in range(int(CELLWIDTH)):
            gridDict[x,y] = 0
    return gridDict

def colourGrid(item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE
    x = x * CELLSIZE
    if lifeDict[item] == 0:
        pygame.draw.rect(screen, WHITE, (x,y, CELLSIZE, CELLSIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(screen, GREEN, (x,y, CELLSIZE, CELLSIZE))
    return None

def getNeighbours(item,lifeDict):
    neighbours = 0
    for x in range(-1,2):
        for y in range(-1,2):
            checkCell = (item[0]+x, item[1]+y)
            if checkCell[0] < CELLWIDTH and checkCell[0] >= 0:
                if checkCell[1] < CELLHEIGHT and checkCell[1] >= 0:
                    if lifeDict[checkCell] == 1:
                        if x == 0 and y == 0:
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours

def tick(lifeDict):
    newTick = {}
    for item in lifeDict:
        numberNeighbours = getNeighbours(item, lifeDict)
        if lifeDict[item] == 1:
            if numberNeighbours < 2:
                newTick[item] = 0
            elif numberNeighbours > 3:
                newTick[item] = 0
            else:
                newTick[item] = 1
        elif lifeDict[item] == 0:
            if numberNeighbours == 3:
                newTick[item] = 1
            else:
                newTick[item] = 0
    return newTick

def startingGridRandom(lifeDict):
    for item in lifeDict:
        lifeDict[item] = random.randint(0,1)
    return lifeDict

def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Game of Life')
    screen.fill(WHITE)
    lifeDict = blankGrid()
    lifeDict = startingGridRandom(lifeDict)
    for item in lifeDict:
        colourGrid(item, lifeDict)

    drawGrid()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()