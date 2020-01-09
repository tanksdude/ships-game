from ships import *
from utils import *
from obstacle import *
from laser import *
import math


def main():
	player = Player_Ship(3, [FIELD_WIDTH-50, FIELD_HEIGHT/2], math.pi/2)
	enemy = Enemy_Ship(3, [100, 100], math.pi/2)
	field_display = pygame.display.set_mode((FIELD_WIDTH, FIELD_HEIGHT))

	def run_game():
			"""contains actions of each frame"""
			run = True
			Obstacle_Manager.init_obstacles()
			while run: 
				pygame.time.delay(DELAY)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
				Laser_Manager.update_lasers(field_display)
				Obstacle_Manager.update_obstacles(field_display)
				player.update_all(field_display)
				pygame.display.update()
				field_display.fill((20,20,20))

			pygame.quit()	

	run_game()

main()

#.       python3 main.py