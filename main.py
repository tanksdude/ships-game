from ships import *
from utils import *
import math


def main():
	player = Player_Ship(3, [50, 50], math.pi/2)
	enemy = Enemy_Ship(3, [100, 100], math.pi/2)
	field_display = pygame.display.set_mode((WIDTH, HEIGHT))

	def run_game():
			"""contains actions of each frame"""
			#add code
			run = True
			while run:
				pygame.time.delay(DELAY)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
				for laser in laser_list: # TODO: move this code somewhere else, like to a class that manages lasers
					laser.update_pos()
					if laser.out_of_bounds():
						laser_list.remove(laser)
						continue
					laser.draw(field_display)
				player.update_all(field_display)
				pygame.display.update()
				field_display.fill((0,0,0))

			pygame.quit()	

	run_game()

main()

#.       python3 main.py