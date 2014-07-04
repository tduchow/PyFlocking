import pygame, sys
from pygame.locals import *


def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos



def render():
    windowSurfaceObj.fill(whiteColor)

    pygame.draw.circle(windowSurfaceObj, redColor, (mousex, mousey), 10)
    pygame.display.update()
    
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

while True:
    
    fpsClock.tick(30) # pause to run the loop at 30 frames per second