import numpy as np
from simulation.player import Player

class World:
	def __init__(self):
		self.player = Player()
		self.enemies = []
		self.projectiles = []
	
	def entries(self):
		return [self.player, *self.enemies, *self.projectiles]

	def update(self, delta):
		for e in self.entries():
			e.update(delta)

