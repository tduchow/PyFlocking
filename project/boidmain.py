import pygame, sys
from pygame.locals import *
from boid import *
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)
NUM_BOIDS = 10
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
        self.font = pygame.font.Font('freesansbold.ttf', 32)

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
            b.update(self.flock, avgelapsed, self.size)     

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

        s = str(constrain_force(Vector2(self.mousex, self.mousey), self.size)) + str((self.mousex, self.mousey))
        self.render_text(ds, s, 10, 10)
        pygame.display.update()
    def render_text(self, ds, s, x, y):
        txt_surf = self.font.render(s, False, pygame.Color(200, 200, 200))
        txt_rect = txt_surf.get_rect()
        txt_rect.topleft = (10, 20)
        ds.blit(txt_surf, txt_rect)

if __name__ == '__main__': main()    
