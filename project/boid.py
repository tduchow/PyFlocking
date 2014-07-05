import pygame
from math import atan2, sqrt
from random import randint
def makeflock(n, w, h, img):
	l = []
	vm = int(sqrt(2)/2*Boid.max_speed) #the max a velocity component can be
	for x in range(n):
		p = Vector2(randint(0, w), randint(0, h))
		v = Vector2(randint(-vm, vm), randint(-vm, vm))
		print(v)
		l.append(Boid(p, v, img))
	return l

class Boid:
	max_speed = 100;#px/s?
	def __init__(self, ipos, ivel, img):
		self.p = ipos
		self.v = ivel
		self.image = img

	def update(self, flock, elapsed):
		self.p += self.v * elapsed;


	def render(self, surface):
		drawimage = pygame.transform.rotate(self.image, -self.v.theta())
		surface.blit(drawimage, (self.p.x, self.p.y))

class Vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def theta(self):
		return atan2(self.y,self.x)/3.1415926*180
	def mag(self):
		return sqrt(self.y**2 + self.x**2)
	def copy(self):
		return Vector2(self.x, self.y)
	def norm(self):
		m = self.mag()
		self.x /= m
		self.y /= m
	def scale(self, factor):
		self.x *= factor
		self.y *= factor
	def setmag(self, newmag):
		self.norm()
		self.scale(newmag)
	def __repr__(self):
		return "(" + str(self.x) + " ," + str(self.y) + ") angle = " + str(self.theta())
	#overloaded vector addition and subraction
	def __add__(self, other):
		return Vector2(self.x+other.x, self.y+other.y)
	def __sub__(self, other):
		return Vector2(self.x-other.x, self.y-other.y)
	def __neg__(self):
		return Vector2(-self.x, -self.y)
	#overloaded scalar multiplication and division
	def __mul__(self, f):
		return Vector2(self.x * f, self.y * f)
	def __div__(self, f):
		return self * (1/f)


