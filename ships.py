

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

	def set_vel(self, new_x_vel, new_y_vel):
		self.x_vel = new_x_vel
		self.y_vel = new_y_vel

	def get_x_vel(self):
		return self.x_vel

	def get_y_vel(self):
		return self.y_vel

	def update_pos(self, x_vel, y_vel):
		self.pos[0] += x_vel
		self.pos[1] += y_vel
		for point in self.vertices:
			point[0] += x_vel
			point[1] += y_vel

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