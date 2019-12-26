

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


class Player_Ship(Ship):

	def control():
		#add code
		return None


class Enemy_Ship(Ship):

	def control():
		#add code
		return None