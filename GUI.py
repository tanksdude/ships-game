from ships import *
from tkinter import *

class Constants:

	FIELD_WIDTH = 300
	FIELD_HEIGHT = 300
	DELAY = 100

class Field(Canvas):

	def __init__(self):
		super().__init__(width=Constants.FIELD_WIDTH, height=Constants.FIELD_HEIGHT)
		self.initBattle()
		self.pack()

	def initBattle(self):
		"""initializes the battlefield"""

		self.create_ships()
		self.draw_ships(self.player, self.enemy)
		self.bind_all("<Key>", self.onKeyPressed)
		self.after(Constants.DELAY, self.onTimer)

	def onTimer(self):
		"""contains actions of each frame"""
		#add code
		self.move_ships(self.player, self.enemy)
		self.draw_ships(self.player, self.enemy)
		self.after(Constants.DELAY, self.onTimer)

	def onKeyPressed(self,e):
		"""handles key presses"""

		key = e.keysym

		W_KEY = 'w'
		if key == W_KEY:
			self.player.set_vel(0, 1)

	def create_ships(self):
		"""instantiates ship objects"""

		self.player = Player_Ship(3, [50, 50], 90)
		self.enemy = Enemy_Ship(3, [100, 100], 90)

	def draw_ships(self, plyr, enmy):
		self.create_polygon(plyr.vertices[0], plyr.vertices[1], plyr.vertices[2],outline='#f11',
    			fill='#1f1', width=2, tag = "plyr_body")
		self.create_polygon(enmy.vertices[0], enmy.vertices[1], enmy.vertices[2],outline='#f11',
    			fill='#1f1', width=2, tag= "enmy_body")
		
	def move_ships(self, plyr, enmy):
		plyr.update_pos(plyr.x_vel, plyr.y_vel)

class GUI(Frame):

	def __init__(self):
		super().__init__()
		self.master.title("Battlefield")
		self.field = Field()
		self.pack()




