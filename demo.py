from demo.demo import start_demo
from simulation.world import World
from simulation.enemy import Enemy
import numpy as np

world = World()

world.enemies = [Enemy(vel=np.random.uniform(0, 1, 2)) for _ in range(5)]

start_demo(world)
