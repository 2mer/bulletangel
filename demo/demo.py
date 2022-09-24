import numpy as np

import cv2 as cv
import numpy as np

from demo.palette import palette
from simulation.world import World
import time

MS_PER_FRAME = int(1 / 60 * 1000)
RENDER_THICKNESS = 2

WINDOW_NAME = 'demo window'

def start_demo(world: World, move_speed=600):
	height=512
	width=512

	# create an image with a uniform color
	empty = np.zeros((height,width,3), np.uint8)
	empty[:] = palette[0]['rgb']

	def render():
		img = empty.copy()

		player = world.player
		center = (int(width // 2) , int(height // 2))
		offset = player.pos - center

		# render player
		cv.circle(img, center, player.rad, palette[1]['rgb'], thickness=RENDER_THICKNESS)
		norm = np.linalg.norm(player.vel)
		if (norm > 0):
			cv.arrowedLine(img, center, (center + (player.vel / (norm) * (player.rad - RENDER_THICKNESS))).astype(int), palette[1]['rgb'], thickness=RENDER_THICKNESS, tipLength=0.35)

		# render enemies
		for e in world.enemies:
			pos = (e.pos - offset).astype(int)
			cv.circle(img, pos, e.rad, palette[2]['rgb'], thickness=RENDER_THICKNESS)
			cv.arrowedLine(img, pos, (pos + (e.vel / (np.linalg.norm(e.vel)) * (e.rad - RENDER_THICKNESS))).astype(int), palette[2]['rgb'], thickness=RENDER_THICKNESS, tipLength=0.35)
			
		# render projectiles
		for p in world.projectiles:
			pos = (p.pos - offset).astype(int)
			cv.circle(img, pos, p.rad, palette[3]['rgb'], thickness=RENDER_THICKNESS)
			cv.arrowedLine(img, pos, (pos + (p.vel / (np.linalg.norm(p.vel)) * (p.rad - RENDER_THICKNESS))).astype(int), palette[3]['rgb'], thickness=RENDER_THICKNESS, tipLength=0.35)


		# show the image
		cv.imshow(WINDOW_NAME, img)
	
	prev_t = time.time()
	while True:
		current_t = time.time()
		world.update(current_t - prev_t)
		prev_t = current_t

		render()

		key = cv.waitKey(MS_PER_FRAME)
		if key == ord('q') and cv.getWindowProperty(WINDOW_NAME, 0) >= 0:
			break
		elif key == ord('w'):
			world.player.vel[1] = -move_speed
		elif key == ord('s'):
			world.player.vel[1] = move_speed
		elif key == ord('a'):
			world.player.vel[0] = -move_speed
		elif key == ord('d'):
			world.player.vel[0] = move_speed
		else:
			world.player.vel *= 0
		

	cv.destroyAllWindows()

def debug():
	height=512
	width=512

	# create an image with a uniform color
	img = np.zeros((height,width,3), np.uint8)
	img[:] = palette[0]['rgb']

	# draw a line
	cv.line(img, (0, 0), (100, 100), palette[1]['rgb'], 5)

	# draw a rectangle
	cv.rectangle(img, (50, 0), (200, 300), palette[2]['rgb'], -1)

	# draw text
	font = cv.FONT_HERSHEY_SIMPLEX
	cv.putText(img, 'OpenCV', (10, 400), font, 4,palette[3]['rgb'],2, cv.LINE_AA)

	# show the image
	cv.imshow('3 Channel Window', img)
	cv.waitKey(0)
	cv.destroyAllWindows()

if __name__ == '__main__':
	debug()
