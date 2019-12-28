from ships import *
import pygame

class Constants:

	FIELD_WIDTH = 300
	FIELD_HEIGHT = 300
	DELAY = 100

class GUI():

	def __init__(self):
		self.run = True
		self.init_battle()
		pygame.init()

	def init_battle(self):
		"""initializes the battlefield"""
		self.create_ships()

	def run_game(self):
		"""contains actions of each frame"""
		#add code
		while self.run:
			pygame.time.delay(Constants.DELAY)


	def create_ships(self):
		"""instantiates ship objects"""

		self.player = Player_Ship(3, [50, 50], 90)
		self.enemy = Enemy_Ship(3, [100, 100], 90)
