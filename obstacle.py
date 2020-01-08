import pygame
from utils import *

class Obstacle():

	def __init__(self, height, width, position):
		self.height = height
		self.width = width
		self.pos = position
		self.color = (255,255,255)
		self.verts = [
			[self.pos[0] + self.width/2, self.pos[1] + self.height/2],
			[self.pos[0] + self.width/2, self.pos[1] - self.height/2],
			[self.pos[0] - self.width/2, self.pos[1] - self.height/2],
			[self.pos[0] - self.width/2, self.pos[1] + self.height/2]
		]

	def draw(self, surface):
		pygame.draw.polygon(surface, self.color, (self.verts[0], self.verts[1], self.verts[2], self.verts[3]))

class Obstacle_Manager():

	obstacle_list = []

	def init_obstacles():
		"""instantiates obstacles at the beginning of the game"""

		return None

	def init_constant_obstacles():
		for x_pos in [100, FIELD_WIDTH - 100]:
			for y_pos in [50, FIELD_HEIGHT - 50]:
				Obstacle_Manager.obstacle_list.append(Obstacle(250, 25, (x_pos, y_pos)))

	def update_obstacles(surface):
		for obstacle in Obstacle_Manager.obstacle_list:
			obstacle.draw(surface)