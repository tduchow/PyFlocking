import pygame, sys
from pygame.locals import *

red = pygame.Color(255, 0, 0)
black = pygame.Color(0, 0, 0)

def main():
    pygame.init()
    size = window_width, window_height = (800, 500)

    g = Game(size, 30)

    g.run()

class Game:
    def __init__(self, size, fps):
        self.size = size
        self.fps = fps
        self.fpsClock = pygame.time.Clock()
        self.drawsurf = pygame.display.set_mode(size);
        self.mousex, self.mousey = 0, 0

    def run(self):
        while True:
            self.checkevents()
            self.update()
            self.render()

    def update(self):
        pass     

    def checkevents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.mousex, self.mousey = event.pos

    def render(self):
        ds = self.drawsurf;
        ds.fill(black)

        pygame.draw.circle(ds, red, (self.mousex, self.mousey), 10)
        pygame.display.update()
    
if __name__ == '__main__': main()    
