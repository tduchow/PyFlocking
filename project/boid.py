import pygame
from math import atan2, sqrt, exp
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
	max_speed = 200#px/s?
	cohesion_factor = .4
	alignment_factor = .0005
	separation_factor = 1
	emergency_factor = 10
	interaction_distance = 75
	interaction_distance_sq = interaction_distance**2
	separation_distance = 30
	separation_distance_sq = separation_distance**2
	emergency_distance = 15
	emergency_distance_sq = emergency_distance**2
	teleport = False
	constrain = not teleport
	def __init__(self, ipos, ivel, img):
		self.p = ipos
		self.v = ivel
		self.image = img

	def update(self, flock, elapsed_time, bounds):
		if Boid.teleport:
			if self.p.x < 0:
				self.p.x = bounds[0]
			elif self.p.x > bounds[0]: 
				self.p.x = 0
			if self.p.y < 0:
				self.p.y = bounds[1]
			elif self.p.y > bounds[1]: 
				self.p.y = 0

		cohere, separate, align = Vector2(), Vector2(), Vector2()
		for other in flock:
			if other != self:
				interaction_count = 0
				separation_count = 0
				#if it's close enough to interact
				if other.p.distancesq(self.p) < Boid.interaction_distance_sq:
					interaction_count+=1
					cohere += other.p
					align += other.v
					#if it's too close
					if other.p.distancesq(self.p) < Boid.separation_distance_sq:
						separation_count += 1
						separate += other.p
						if other.p.distancesq(self.p) < Boid.emergency_distance_sq:
							separate += other.p*Boid.emergency_factor
		if interaction_count>0:
			cohere /= interaction_count
			align /= interaction_count
		if separation_count>0:
			separate /= separation_count
		#cohere is now the center of mass of boids we want to be closer to, the next line makes it a vector pointing toward that point
		cohere = cohere - self.p
		cohere *= Boid.cohesion_factor
		#separate is now the center of mass of boids we need to move away from, same deal
		separate = separate - self.p
		separate *= Boid.separation_factor
		#align is now the average velocity of the nearby boids, for now, we'll just add that?
		acceleration = cohere + align - separate
		# print(acceleration)
		# print('\n'.join(['C: ' + str(cohere), 'A: ' + str(align), 'S: ' + str(separate)]))
		if Boid.constrain:
			acceleration+=constrain_force(self.p, bounds)

		self.v += acceleration
		self.v.limit(Boid.max_speed)
		self.p += self.v * elapsed_time;


	def render(self, surface):
		drawimage = pygame.transform.rotate(self.image, -self.v.theta())
		surface.blit(drawimage, (self.p.x, self.p.y))
def constrain_force(p, bounds):
	centerpoint = Vector2(*bounds)/2
	centerer = (centerpoint-p).norm()
	xforce = 1.3**(abs(p.x - centerpoint.x)-centerpoint.x)
	yforce = 1.3**(abs(p.y - centerpoint.y)-centerpoint.y)
	centerer.x *= xforce
	centerer.y *= yforce
	return centerer

class Vector2:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	def theta(self):
		return atan2(self.y,self.x)/3.1415926*180
	def magsq(self):
		return self.y**2 + self.x**2
	def mag(self):
		return sqrt(self.magsq())
	def copy(self):
		return Vector2(self.x, self.y)
	def norm(self):
		m = self.mag()
		self.x /= m
		self.y /= m
		return self
	def scale(self, factor):
		self.x *= factor
		self.y *= factor
		return self

	def setmag(self, newmag):
		self.norm()
		self.scale(newmag)
	def distancesq(self, other):
		return (self.x-other.x)**2 + (self.y-other.y)**2
	def distance(self, other):
		return sqrt(self.distancesq(other))
	def limit(self, max):
		if self.magsq()>max**2:
			self.setmag(max)

	def __repr__(self):
		return "(" + str(self.x)[0:5] + " , " + str(self.y)[0:5] + "): R = " + str(self.mag())[0:5]+ ", θ = " + str(self.theta())[0:6] + "°"

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
	def __truediv__(self, f):
		return self * (1/f)


