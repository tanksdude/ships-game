from ships import *
from utils import *
import math
import laser


def main():
	player = Player_Ship(3, [50, 50], math.pi/2)
	enemy = Enemy_Ship(3, [100, 100], math.pi/2)
	field_display = pygame.display.set_mode((WIDTH, HEIGHT))

	def run_game():
			"""contains actions of each frame"""
			run = True
			while run:
				pygame.time.delay(DELAY)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
				Laser_Manager.update_lasers(field_display)
				player.update_all(field_display)
				pygame.display.update()
				field_display.fill((20,20,20))

			pygame.quit()	

	run_game()

main()

#.       python3 main.py