from ships import *
from utils import *
from obstacle import *
from laser import *
import math
import collision as coll


def main():
	player = Player_Ship(3, [FIELD_WIDTH-50, FIELD_HEIGHT/2], math.pi/2)
	enemy = Enemy_Ship(3, [100, 100], math.pi/2)
	field_display = pygame.display.set_mode((FIELD_WIDTH, FIELD_HEIGHT))

	def laser_obstacle_collision():
		for (laser, coll_laser) in zip(Laser_Manager.laser_list, Laser_Manager.collision_laser_list):
			for coll_obstacle in Obstacle_Manager.collision_obstacle_list:
				if coll.collide(coll_laser, coll_obstacle):
					Laser_Manager.laser_list.remove(laser)
					Laser_Manager.collision_laser_list.remove(coll_laser)
					break



	def run_game():
			"""contains actions of each frame"""
			run = True
			Obstacle_Manager.init_obstacles()
			while run: 
				pygame.time.delay(DELAY)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
				player.update_all(field_display)
				Laser_Manager.update_lasers(field_display)
				Obstacle_Manager.update_obstacles(field_display)
				laser_obstacle_collision()
				pygame.display.update()
				field_display.fill((20,20,20))

			pygame.quit()	

	run_game()

main()

#.       python3 main.py

