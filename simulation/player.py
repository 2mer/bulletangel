import numpy as np
from simulation.game_object import GameObject

class Player(GameObject):
	def __init__(self, health=0, **kwargs):
		super().__init__(**kwargs)
        
		self.health = health