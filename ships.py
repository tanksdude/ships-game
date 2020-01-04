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
	attack_mode_key_toggle = True # updates when the attack mode key goes up or down
	attack_mode_key_toggle_other = True # updates when ↑ changes, so the end effect is this changes when the key goes down
	attack_mode_last_state = True
	power_up = None

	def __init__(self, health, position, direction):
		self.hp = health
		self.pos = position
		self.dir = direction
		self.verts = [
			[self.pos[0],   self.pos[1]-10],
			[self.pos[0]+5, self.pos[1]+5],
			[self.pos[0]-5, self.pos[1]+5]
		]
		self.vel = [0, 0]
		self.ang_vel = 0
		self.lasers_fired = []
		self.color = (255, 255, 255)

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
		self.dir %= 2 * math.pi
		for point in self.verts:
			diff_x = point[0] - self.pos[0]
			diff_y = point[1] - self.pos[1]
			point[0] = self.pos[0] + diff_x * math.cos(self.ang_vel) - diff_y * math.sin(self.ang_vel)
			point[1] = self.pos[1] + diff_x * math.sin(self.ang_vel) + diff_y * math.cos(self.ang_vel)
	
	def draw(self, surface):
		pygame.draw.polygon(surface, self.color, (self.verts[0], self.verts[1], self.verts[2]))

class Player_Ship(Ship):

	def __init__(self, health, position, direction):
		super().__init__(health, position, direction)
		self.color = (255, 0, 0)

	def mode_update(self):
		"""changes the ship's mode based on if "e" is pressed"""

		keys = pygame.key.get_pressed()
		new_attack_mode_state = not keys[pygame.K_e]

		if self.attack_mode_last_state != new_attack_mode_state:
			self.attack_mode_key_toggle = not self.attack_mode_key_toggle
			if self.attack_mode_key_toggle:
				self.attack_mode_key_toggle_other = not self.attack_mode_key_toggle_other
		
		if self.attack_mode_key_toggle_other:
			self.attack_mode = new_attack_mode_state
		
		#print(self.attack_mode_last_state, self.attack_mode_key_toggle, self.attack_mode_key_toggle_other, new_attack_mode_state)

		self.attack_mode_last_state = new_attack_mode_state

	def vel_update(self):
		"""determines how to update the ship's velocity based on its mode"""

		keys = pygame.key.get_pressed()
		self.mode_update()

		def attack_mode_vel_update():
			"""changes the ship velocity in attack mode based on user input"""

			vel = [0, 0] # x and y components relative to actual ship

			if keys[pygame.K_d]:
				vel[0] += Ship.speed
			if keys[pygame.K_a]:
				vel[0] -= Ship.speed
			if keys[pygame.K_w]:
				vel[1] += Ship.speed
			if keys[pygame.K_s]:
				vel[1] -= Ship.speed
			
			# translate relative velocity into true velocity
			self.set_x_vel(x_comp(vel[0], self.dir - math.pi/2) + x_comp(-vel[1], self.dir))
			self.set_y_vel(y_comp(vel[0], self.dir - math.pi/2) + y_comp(-vel[1], self.dir))

			#print(vel[0], vel[1])

		def speed_mode_vel_update():
			"""changes the ship velocity in speed mode based on user input"""
			
			if keys[pygame.K_w]:
				self.set_x_vel(- x_comp(Ship.speed * 2, self.dir))
				self.set_y_vel(- y_comp(Ship.speed * 2, self.dir))
			else:
				self.vel = [0, 0]

		if self.attack_mode:
			attack_mode_vel_update()
		else:
			speed_mode_vel_update()

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

		self.lasers_fired.append(Laser(self.pos[:], self.dir, (255, 0, 0)))

	def update_lasers(self):
		"""fires laser if player presses space and updates all lasers fired by the player"""

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			self.fire_laser()
		for laser in self.lasers_fired:
			laser.update_pos()
			if laser.out_of_bounds():
				self.lasers_fired.remove(laser)

		#print(len(self.lasers_fired))

	def update_all(self, field_display):
		self.vel_update()
		self.ang_vel_update()
		self.update_pos()
		self.update_dir()
		self.draw(field_display)
		self.update_lasers()
		for laser in self.lasers_fired:
			laser.draw(field_display)

class Enemy_Ship(Ship):

	def control(self):
		#add code
		return None

