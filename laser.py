import pygame
from utils import *

class Laser():

	power = 3
	speed = 600 / DELAY
	radius = 2

	def __init__(self, position, direction, color):
		self.pos = position
		self.dir = direction
		self.vel = [- x_comp(Laser.speed, self.dir), - y_comp(Laser.speed, self.dir)]
		self.color = color
    
	def update_pos(self):
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]

	def out_of_bounds(self):
		return (self.pos[0] - self.radius < 0) or (self.pos[0] + self.radius > WIDTH) or (self.pos[1] - self.radius < 0) or (self.pos[1] + self.radius > HEIGHT)

	def draw(self, surface):
		updated_pos = [int(self.pos[0]), int(self.pos[1])]
		pygame.draw.circle(surface, self.color, updated_pos, Laser.radius)

class Laser_Manager():

	laser_list = []

	def update_lasers(surface):
		for laser in Laser_Manager.laser_list:
				laser.update_pos()
				if laser.out_of_bounds():
					Laser_Manager.laser_list.remove(laser)
					continue
				laser.draw(surface)