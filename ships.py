import pygame

class Ship():

	health = 0
	speed = 1
	damage = 1
	mode = 'attack'
	power_up = None

	def __init__(self, health, position, direction):
		self.hp = health
		self.pos = position
		self.dir = direction
		self.vertices = [
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

	def update_pos(self, x_vel, y_vel):
		self.pos[0] += x_vel
		self.pos[1] += y_vel
		for point in self.vertices:
			point[0] += x_vel
			point[1] += y_vel

	def rotate():
		return None


class Player_Ship(Ship):

	def check_input(self):
		#add code
		keys = pygame.key.get_pressed()


class Enemy_Ship(Ship):

	def control(self):
		#add code
		return None

