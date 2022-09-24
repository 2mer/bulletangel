import torch
import torch.nn as nn

from simulation import simulation

device = 'cuda' if torch.cuda.is_available() else 'cpu'

