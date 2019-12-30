from ships import *
from GUI import *


def main():
	player = Player_Ship(3, [50, 50], 90)
	enemy = Enemy_Ship(3, [100, 100], 90)
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
				update_objects()
				pygame.display.update()
				field_display.fill((0,0,0))

			pygame.quit()

	def update_objects():
		player.vel_update()
		player.ang_vel_update()
		player.update_pos()
		player.update_dir()
		player.draw(field_display, (255, 0, 0))

	run_game()



main()

#python3 main.py