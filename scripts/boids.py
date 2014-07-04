import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
size = window_width, window_height = (800, 500)

windowSurfaceObj = pygame.display.set_mode(size)
pygame.display.set_caption('Basic')

redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
blueColor = pygame.Color(0, 0, 255)
whiteColor = pygame.Color(255, 255, 255)
mousex, mousey = 0, 0

r = 10

while True:
    windowSurfaceObj.fill(whiteColor)

    pygame.draw.circle(windowSurfaceObj, redColor, (mousex, mousey), r)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if event.button in (1, 2, 3):
                msg = 'left, middle, or right mouse click'
            elif event.button in (4, 5):
                if event.button == 4:
                    r -=1
                else:
                    r+=1
                msg = 'mouse scrolled up or down'

        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                msg = 'Arrow key pressed.'
            if event.key == K_a:
                msg = '"A" key pressed'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    fpsClock.tick(30) # pause to run the loop at 30 frames per second