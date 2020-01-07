import pygame

class Obstacle():

	def __init__(self, length, width, position):
		self.length = length
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
		pygame.draw.polygon(surface, self.color, self.verts[0] self.verts[1] self.verts[2] self.verts[3])