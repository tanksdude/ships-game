import pygame
from utils import *
import math
from laser import *

class Ship():

	health = 0
	speed = 200 / DELAY
	diagonal_speed = speed / (2 ** (1/2)) 
	damage = 1
	attack_mode = True
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
		self.lasers_fired = []

	def set_x_vel(self, new_x_vel):
		self.vel[0] = new_x_vel

	def set_y_vel(self, new_y_vel):
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

	def mode_update(self):
		"""changes the ship's mode based on if "e" is pressed"""

		keys = pygame.key.get_pressed()
		if keys[pygame.K_e]:
	 		self.attack_mode = False
		else:
		 	self.attack_mode = True

	def vel_update(self):
		"""determines how to update the ship's velocity based on its mode"""

		self.mode_update()
		if self.attack_mode:
			self.attack_mode_vel_update()
		else:
			self.speed_mode_vel_update()

	def attack_mode_vel_update(self):
		"""changes the ship velocity in attack mode based on user input"""

		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.set_x_vel(y_comp(Ship.speed, self.dir))
			self.set_y_vel(- x_comp(Ship.speed, self.dir))
			if keys[pygame.K_w]:
				self.set_x_vel(y_comp(Ship.diagonal_speed, self.dir) - x_comp(Ship.diagonal_speed, self.dir))
				self.set_y_vel(- x_comp(Ship.diagonal_speed, self.dir) - y_comp(Ship.diagonal_speed, self.dir))
			elif keys[pygame.K_s]:
				self.set_x_vel(y_comp(Ship.diagonal_speed, self.dir) + x_comp(Ship.diagonal_speed, self.dir))
				self.set_y_vel(- x_comp(Ship.diagonal_speed, self.dir) + y_comp(Ship.diagonal_speed, self.dir))
		elif keys[pygame.K_a]:
			self.set_x_vel(- y_comp(Ship.speed, self.dir))
			self.set_y_vel(x_comp(Ship.speed, self.dir))
			if keys[pygame.K_w]:
				self.set_x_vel(- x_comp(Ship.diagonal_speed, self.dir) - y_comp(Ship.diagonal_speed, self.dir))
				self.set_y_vel(x_comp(Ship.diagonal_speed, self.dir) - y_comp(Ship.diagonal_speed, self.dir))
			elif keys[pygame.K_s]:
				self.set_x_vel(- y_comp(Ship.diagonal_speed, self.dir) + x_comp(Ship.diagonal_speed, self.dir))
				self.set_y_vel(x_comp(Ship.diagonal_speed, self.dir) + y_comp(Ship.diagonal_speed, self.dir))
		elif keys[pygame.K_w]:
			self.set_x_vel(- x_comp(Ship.speed, self.dir))
			self.set_y_vel(- y_comp(Ship.speed, self.dir))
		elif keys[pygame.K_s]:
			self.set_x_vel(x_comp(Ship.speed, self.dir))
			self.set_y_vel(y_comp(Ship.speed, self.dir))
		else:
			self.vel = [0, 0]

	def speed_mode_vel_update(self):
		"""changes the ship velocity in speed mode based on user input"""

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.set_x_vel(- x_comp(Ship.speed * 2, self.dir))
			self.set_y_vel(- y_comp(Ship.speed * 2, self.dir))
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

	def fire_laser(self):
		"""fires by initializing a laser object and storing it in the ship's fired lasers"""

		self.lasers_fired.append(Laser(self.pos[:], self.dir))

	def update_lasers(self):
		"""fires laser if player presses space and updates all lasers fired by the player"""

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			self.fire_laser()
		for laser in self.lasers_fired:
			laser.update_pos()

	def update_all(self, field_display):
		self.vel_update()
		self.ang_vel_update()
		self.update_pos()
		self.update_dir()
		self.draw(field_display, (255, 0, 0))
		self.update_lasers()
		for laser in self.lasers_fired:
			laser.draw(field_display, (255, 0, 0))

class Enemy_Ship(Ship):

	def control(self):
		#add code
		return None

