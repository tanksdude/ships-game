import pygame
from GUI import *

class Ship():

	health = 0
	speed = 2
	damage = 1
	mode = 'attack'
	power_up = None

	def __init__(self, health, position, direction):
		self.hp = health
		self.pos = position
		self.dir = direction
		self.verts = [
							[self.pos[0], self.pos[1]-10],
							[self.pos[0]+5, self.pos[1]+5],
							[self.pos[0]-5, self.pos[1]+5]
						]
		self.vel = [0, 0]

	def set_vel(self, new_x_vel, new_y_vel):
		self.vel[0] = new_x_vel
		self.vel[1] = new_y_vel

	def get_x_vel(self):
		return self.vel[0]

	def get_y_vel(self):
		return self.vel[1]

	def get_x_pos(self):
		return self.pos[0]

	def get_y_pos(self):
		return self.pos[1]

	def update_pos(self):
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]
		for point in self.verts:
			point[0] += self.vel[0]
			point[1] += self.vel[1]

	def draw(self, surface, color):
		pygame.draw.polygon(surface, color, (self.verts[0], self.verts[1], self.verts[2]))

class Player_Ship(Ship):

	def check_input(self):
		#add code
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.vel[0] = Ship.speed
		elif keys[pygame.K_a]:
			self.vel[0] = -Ship.speed
		else:
			self.vel[0] = 0
		if keys[pygame.K_w]:
			self.vel[1] = -Ship.speed
		elif keys[pygame.K_s]:
			self.vel[1] = Ship.speed
		else:
			self.vel[1] = 0


class Enemy_Ship(Ship):

	def control(self):
		#add code
		return None

