import torch
from nets.reg import RegressionModel

if __name__ == '__main__':
	in_features = 100
	out_features = 20
	batch_size = 10

	net = RegressionModel(in_features, out_features)
	
	x = torch.randn((batch_size, in_features))
	y = net(x)
	print(f'input shape: {x.shape}')
	print(f'output shape: {y.shape}')

	# TODO: shape of chosen action
