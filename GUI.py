from ships import *
from tkinter import *

class Constants:

	FIELD_WIDTH = 300
	FIELD_HEIGHT = 300
	DELAY = 100

class Field(Canvas):

	def __init__(self):
		super().__init__(width=Constants.FIELD_WIDTH, heigh=Constants.FIELD_HEIGHT)
		self.initBattle()
		self.pack()

	def initBattle(self):
		"""initializes the battlefield"""

		self.create_ships()
		self.draw_ships(self.player, self.enemy)
		self.after(Constants.DELAY, self.onTimer)

	def onTimer(self):
		"""contains actions of each frame"""
		#add code
		self.after(Constants.DELAY, self.onTimer)

	def create_ships(self):
		self.player = Player_Ship(3, [50, 50], 90)
		self.enemy = Enemy_Ship(3, [100, 100], 90)

	def draw_ships(self, *args):
		for ship in args:
			self.create_polygon(ship.vertices[0], ship.vertices[1], ship.vertices[2],outline='#f11',
    fill='#1f1', width=2)
		

class GUI(Frame):

	def __init__(self):
		super().__init__()
		self.master.title("Battlefield")
		self.field = Field()
		self.pack()




