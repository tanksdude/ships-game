import pygame
from utils import *
import math
from laser import *

class Ship():

	health = 0
	width = 15
	height = 25
	speed = 300 / DELAY
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
		self.body_verts = [
			[self.pos[0],   self.pos[1] - 4/5 * Ship.height],
			[self.pos[0] + Ship.width/2 , self.pos[1] + 1/5 * Ship.height],
			[self.pos[0] - Ship.width/2, self.pos[1] + 1/5 * Ship.height]
		]
		self.init_attack_gear()
		self.vel = [0, 0]
		self.ang_vel = 0
		self.lasers_fired = []
		self.color = (255, 255, 255)
		self.gun_color = (100, 100, 100)

	def set_x_vel(self, new_x_vel):
		self.vel[0] = new_x_vel

	def set_y_vel(self, new_y_vel):
		self.vel[1] = new_y_vel	

	def init_attack_gear(self):
		self.r_wing_verts = [
			[self.pos[0] + Ship.width / 4, self.pos[1]],
			[self.pos[0] + 5/8 * Ship.width, self.pos[1]],
			[self.pos[0] + Ship.width / 8, self.pos[1] - 2/5 * Ship.height]
		]
		rotate_vertices(self.r_wing_verts, self.pos, self.dir - math.pi/2)
		self.l_wing_verts = [
			[self.pos[0] - Ship.width / 4, self.pos[1]],
			[self.pos[0] - 5/8 * Ship.width, self.pos[1]],
			[self.pos[0] - Ship.width / 8, self.pos[1] - 2/5 * Ship.height]
		]
		rotate_vertices(self.l_wing_verts, self.pos, self.dir - math.pi/2)
		self.r_gun_verts = [
			[self.pos[0] + 3/8 * Ship.width, self.pos[1]],
			[self.pos[0] + Ship.width/2, self.pos[1]],
			[self.pos[0] + Ship.width/2, self.pos[1] - 3/5 * Ship.height],
			[self.pos[0] + 3/8 * Ship.width, self.pos[1] - 3/5 * Ship.height]
		]
		rotate_vertices(self.r_gun_verts, self.pos, self.dir - math.pi/2)
		self.l_gun_verts = [
			[self.pos[0] - 3/8 * Ship.width, self.pos[1]],
			[self.pos[0] - Ship.width/2, self.pos[1]],
			[self.pos[0] - Ship.width/2, self.pos[1] - 3/5 * Ship.height],
			[self.pos[0] - 3/8 * Ship.width, self.pos[1] - 3/5 * Ship.height]
		]
		rotate_vertices(self.l_gun_verts, self.pos, self.dir - math.pi/2)

	def update_pos(self):
		"""updates the position of the ship based on its velocity"""

		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]
		def update_vert_pos(vertices):
			for point in vertices:
				point[0] += self.vel[0]
				point[1] += self.vel[1]

		update_vert_pos(self.body_verts)
		if self.attack_mode:
			update_vert_pos(self.r_wing_verts)
			update_vert_pos(self.l_wing_verts)
			update_vert_pos(self.r_gun_verts)
			update_vert_pos(self.l_gun_verts)

	def update_dir(self):
		"""updates the direction and calculates new vertices using the rotation matrix"""

		self.dir += self.ang_vel
		self.dir %= 2 * math.pi

		rotate_vertices(self.body_verts, self.pos, self.ang_vel)
		if self.attack_mode:
			rotate_vertices(self.r_wing_verts, self.pos, self.ang_vel)
			rotate_vertices(self.l_wing_verts, self.pos, self.ang_vel)
			rotate_vertices(self.r_gun_verts, self.pos, self.ang_vel)
			rotate_vertices(self.l_gun_verts, self.pos, self.ang_vel)
	
	def draw(self, surface):
		pygame.draw.polygon(surface, self.color, (self.body_verts[0], self.body_verts[1], self.body_verts[2]))
		if self.attack_mode:
			pygame.draw.polygon(surface, self.gun_color, (self.r_gun_verts[0], self.r_gun_verts[1], self.r_gun_verts[2], self.r_gun_verts[3]))
			pygame.draw.polygon(surface, self.gun_color, (self.l_gun_verts[0], self.l_gun_verts[1], self.l_gun_verts[2], self.l_gun_verts[3]))
			pygame.draw.polygon(surface, self.color, (self.r_wing_verts[0], self.r_wing_verts[1], self.r_wing_verts[2]))
			pygame.draw.polygon(surface, self.color, (self.l_wing_verts[0], self.l_wing_verts[1], self.l_wing_verts[2]))

class Player_Ship(Ship):

	def __init__(self, health, position, direction):
		super().__init__(health, position, direction)
		self.color = (0, 0, 255)

	def mode_update(self):
		"""changes the ship's mode if 'e' is pressed"""

		keys = pygame.key.get_pressed()
		new_attack_mode_state = not keys[pygame.K_e]

		if self.attack_mode_last_state != new_attack_mode_state:
			self.attack_mode_key_toggle = not self.attack_mode_key_toggle
			if self.attack_mode_key_toggle:
				self.attack_mode_key_toggle_other = not self.attack_mode_key_toggle_other
				self.init_attack_gear()
		
		if self.attack_mode_key_toggle_other:
			self.attack_mode = new_attack_mode_state
		
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
			
			# normalize velocity
			magnitude = (vel[0]**2 + vel[1]**2) ** .5
			if magnitude > Ship.speed:
				magnitude /= Ship.speed # make the magnitude relative to Ship.speed
				vel[0] /= magnitude
				vel[1] /= magnitude
			
			# translate relative velocity into true velocity
			self.set_x_vel(x_comp(vel[0], self.dir - math.pi/2) + x_comp(-vel[1], self.dir))
			self.set_y_vel(y_comp(vel[0], self.dir - math.pi/2) + y_comp(-vel[1], self.dir))

		def speed_mode_vel_update():
			"""changes the ship velocity in speed mode based on user input"""
			
			vel = [0, 0]
			if keys[pygame.K_w]:
				vel[1] += 2 * Ship.speed
			self.set_x_vel(x_comp(vel[0], self.dir - math.pi/2) + x_comp(-vel[1], self.dir))
			self.set_y_vel(y_comp(vel[0], self.dir - math.pi/2) + y_comp(-vel[1], self.dir))

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

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.attack_mode:
			Laser_Manager.laser_list.append(Laser(self.r_gun_verts[3][:], self.dir, (255, 0, 0)))
			Laser_Manager.laser_list.append(Laser(self.l_gun_verts[3][:], self.dir, (255, 0, 0)))

	def update_all(self, field_display):
		self.vel_update()
		self.ang_vel_update()
		self.update_pos()
		self.update_dir()
		self.draw(field_display)
		self.fire_laser()

class Enemy_Ship(Ship):

	def control(self):
		#add code
		return None

