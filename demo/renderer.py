import cv2 as cv
import numpy as np

palette = {
	'Portland Orange': (244, 96, 54),
	'Steel Blue': (91, 133, 170),
	'Purple Navy': (65, 71, 112),
	'Russian Violet': (55, 34, 72),
	'Xiketic': (23, 17, 35),
}

def rotation_matrix(rad):
	c = np.cos(-rad)
	s = np.sin(-rad)
	return np.array([
		[c, -s, 0.0],
		[s, c, 0.0],
		[0.0, 0.0, 1.0],
	])

def translation_matrix(dx, dy):
	return np.array([
		[1.0, 0.0, -dx],
		[0.0, 1.0, -dy],
		[0.0, 0.0, 1.0],
	])

def projection_matrix(cw, ch):
	return np.array([
		[1.0 / cw, 0.0, 0.0]
		[0.0, 1.0 / ch, 0.0],
		[0.0, 0.0, 1.0]
	])

class DemoRenderer:
	def __init__(
			self,
			camera_pos=np.zeros(2),
			camera_size=np.ones(2),
			camera_rotation=0,
			window_size=(512, 512),
			fps=60,
			window_name='demo window',
			bg_color=np.zeros(3)
			):
		self.camera_pos = camera_pos
		self.camera_size = camera_size
		self.camera_rotation = camera_rotation
		self.window_size = window_size
		self.fps = fps
		self.window_name = window_name

		self.blank = np.zeros((window_size[0], window_size[1], 3))
		self.blank += bg_color

		self.update_combined()

	def line(self, from_vec, to_vec, color='r'):
		from_vec = self.project(from_vec)
		to_vec = self.project(to_vec)
		cv.arrowedLine(
			self.window_name,
			from_vec,
			to_vec,
			palette[2]['rgb'], thickness=RENDER_THICKNESS, tipLength=0.35)

	def project(self, v):
		# (-1, -1) to (1, 1)
		v = self.combined @ np.array([v[0], v[1], 1.0])
		# (0, 0) to (w, h)
		v = (v * 0.5 + 0.5) * self.window_size
		return (int(v[0]), int(v[1]))

	def update_combined(self):
		self.combined = (
			projection_matrix(
				self.camera_size[0], 
				self.camera_size[1], 
				self.window_size[0], 
				self.window_size[1]
			) @ 
			rotation_matrix(self.camera_rotation) @ 
			translation_matrix(self.camera_pos[0], self.camera_pos[1])
		)

	def wait(self):
		pass