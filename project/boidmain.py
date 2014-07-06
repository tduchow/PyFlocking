import pygame, sys
from pygame.locals import *
from boid import *
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)
NUM_BOIDS = 25
def main():
    pygame.init()
    size = window_width, window_height = (1000, 600)
    g = Game(size, 30)
    g.run()

class Game:
    def __init__(self, size, fps):
        self.size = size
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.drawsurf = pygame.display.set_mode(size);
        self.mousex, self.mousey = 0, 0
        self.boid_image = pygame.image.load('TriBoid.png')
        self.boid_image = pygame.transform.smoothscale(self.boid_image, (20, 15))
        self.flock = makeflock(NUM_BOIDS, size[0], size[1], self.boid_image)

    def run(self):
        while True:
            self.checkevents()
            self.update()
            self.render()
            self.clock.tick(self.fps)

    def update(self):
        avgfps = self.clock.get_fps()#the average fps over the last 10 frames.
        if avgfps>0:#Basically after the first 10 frames
            avgelapsed = 1/avgfps
        else:
            avgelapsed = 1/self.fps
        for b in self.flock:
            b.update(self.flock, avgelapsed)     

    def checkevents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.mousex, self.mousey = event.pos

    def render(self):
        ds = self.drawsurf;
        ds.fill(BLACK)
        ds.blit(self.boid_image, (self.mousex - self.boid_image.get_width()/2, self.mousey-self.boid_image.get_height()/2))
        #pygame.draw.circle(ds, RED, (self.mousex, self.mousey), 10)
        for b in self.flock:
            b.render(ds);

        pygame.display.update()
    
if __name__ == '__main__': main()    
