import pygame, sys
from pygame.locals import *


def update():
    #check events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            global mousex, mousey
            mousex, mousey = event.pos



def render():
    winsurf.fill(black)

    pygame.draw.circle(winsurf, red, (mousex, mousey), 10)
    pygame.display.update()
    
pygame.init()
fpsClock = pygame.time.Clock()
size = window_width, window_height = (800, 500)

winsurf = pygame.display.set_mode(size)
pygame.display.set_caption('Basic')

red = pygame.Color(255, 0, 0)

black = pygame.Color(0, 0, 0)
mousex, mousey = 0, 0

while True:
    update()
    render()
    fpsClock.tick(30) # pause to run the loop at 30 frames per second