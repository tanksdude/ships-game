import pygame
from utils import *

class Laser():

	power = 3
	speed = 600 / DELAY
	radius = 2

	def __init__(self, position, direction):
		self.pos = position
		self.dir = direction
		self.vel = [- x_comp(Laser.speed, self.dir), - y_comp(Laser.speed, self.dir)]

	def draw(self, surface, color):
		self.pos[0] = int(self.pos[0])
		self.pos[1] = int(self.pos[1])
		pygame.draw.circle(surface, color, self.pos, Laser.radius)

	def update_pos(self):
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]

	def out_of_bounds(self):
		return (self.pos[0] - self.radius < 0) or (self.pos[0] + self.radius > WIDTH) or (self.pos[1] - self.radius < 0) or (self.pos[1] + self.radius > HEIGHT)

