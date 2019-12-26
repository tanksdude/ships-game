

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
		self.x_vel = 0
		self.y_vel = 0

	def update_pos(self, x_vel, y_vel):
		self.pos[0] += self.x_vel
		self.pos[1] += self.y_vel

	def rotate():
		return None


class Player_Ship(Ship):

	def control():
		#add code
		return None


class Enemy_Ship(Ship):

	def control():
		#add code
		return None