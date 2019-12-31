import pygame
from GUI import *
import math

class Ship():

	health = 0
	speed = 200 / DELAY
	diagonal_speed = speed / (2 ** (1/2)) 
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
		self.ang_vel = 0

	def set_vel(self, new_x_vel, new_y_vel):
		self.vel[0] = new_x_vel
		self.vel[1] = new_y_vel

	def update_pos(self):
		"""updates the position of the ship based on its velocity"""

		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]
		for point in self.verts:
			point[0] += self.vel[0]
			point[1] += self.vel[1]

	def update_dir(self):
		"""updates the direction and calculates new vertices using the rotation matrix"""

		self.dir += self.ang_vel
		if self.dir == 2 * math.pi:
			self.dir = 0
		for point in self.verts:
			diff_x = point[0] - self.pos[0]
			diff_y = point[1] - self.pos[1]
			point[0] = self.pos[0] + diff_x * math.cos(self.ang_vel) - diff_y * math.sin(self.ang_vel)
			point[1] = self.pos[1] + diff_x * math.sin(self.ang_vel) + diff_y * math.cos(self.ang_vel)
	
	def draw(self, surface, color):
		pygame.draw.polygon(surface, color, (self.verts[0], self.verts[1], self.verts[2]))

class Player_Ship(Ship):

	def vel_update(self):
		"""changes the ship velocity based on user input"""

		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.vel[0] = Ship.speed * math.sin(self.dir)
			self.vel[1] = - Ship.speed * math.cos(self.dir)
			if keys[pygame.K_w]:
				self.vel[0] = Ship.diagonal_speed * math.sin(self.dir) - Ship.diagonal_speed * math.cos(self.dir)
				self.vel[1] = - Ship.diagonal_speed  * math.cos(self.dir) - Ship.diagonal_speed * math.sin(self.dir)
			elif keys[pygame.K_s]:
				self.vel[0] = Ship.diagonal_speed * math.sin(self.dir) + Ship.diagonal_speed * math.cos(self.dir)
				self.vel[1] = - Ship.diagonal_speed * math.cos(self.dir) + Ship.diagonal_speed * math.sin(self.dir)
		elif keys[pygame.K_a]:
			self.vel[0] = - Ship.speed * math.sin(self.dir)
			self.vel[1] = Ship.speed * math.cos(self.dir)
			if keys[pygame.K_w]:
				self.vel[0] = - Ship.diagonal_speed * math.cos(self.dir) - Ship.diagonal_speed * math.sin(self.dir)
				self.vel[1] = Ship.diagonal_speed * math.cos(self.dir) - Ship.diagonal_speed * math.sin(self.dir)
			elif keys[pygame.K_s]:
				self.vel[0] = - Ship.diagonal_speed * math.sin(self.dir) + Ship.diagonal_speed * math.cos(self.dir)
				self.vel[1] = Ship.diagonal_speed * math.cos(self.dir) + Ship.diagonal_speed * math.sin(self.dir)
		elif keys[pygame.K_w]:
			self.vel[0] = - Ship.speed * math.cos(self.dir)
			self.vel[1] = - Ship.speed * math.sin(self.dir)
		elif keys[pygame.K_s]:
			self.vel[0] = Ship.speed * math.cos(self.dir)
			self.vel[1] = Ship.speed * math.sin(self.dir)
		else:
			self.vel = [0, 0]

	def ang_vel_update(self):
		"""changes the ship angular velocity based on user input"""
 
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.ang_vel = - math.pi / 10
		elif keys[pygame.K_RIGHT]:
			self.ang_vel = math.pi / 10
		else:
			self.ang_vel = 0


class Enemy_Ship(Ship):

	def control(self):
		#add code
		return None

