import numpy as np

class GameObject:
	def __init__(
			self,
			pos=np.array((0, 0),
			dtype='float64'),
			rad=1,
			vel=np.array((0, 0), dtype='float64')
			):
		self.pos = pos
		self.rad = rad
		self.vel = vel
	
	def update(self, delta: float):
		self.pos += self.vel * delta
