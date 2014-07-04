import pygame
from math import atan, sqrt
class Boid:
	def __init__(self, ipos, ivel, img):
		self.p = ipos
		self.v = ivel
		self.image = img

	def update(self, flock):
		pass

	def render(self, surface):
		surface.blit(pygame.transform.rotate(self.image, self.v.theta()), (self.p.x, self.p.y))

class Vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def theta(self):
		return atan(self.y/self.x)
	def mag(self):
		return sqrt(self.y**2 + self.x**2)
	def copy(self):
		return Vector2(self.x, self.y)
	def norm(self):
		m = mag()
		self.x /= m
		self.y /= m
	def scale(self, factor):
		self.x *= factor
		self.y *= factor
	def setmag(self, newmag):
		norm()
		scale(newmag)


