import numpy as np
from game_object import GameObject

class Projectile(GameObject):
	def __init__(self, lifetime=0, damage=0, **kwargs):
		super().__init__(**kwargs)
		
		self.lifetime = lifetime
		self.damage = damage
