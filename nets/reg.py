import torch.nn as nn

class RegressionModel(nn.Module):
	def __init__(self,
			in_features,
			out_features,
			hidden_features=64,
			hidden_layers=3,
			non_linearity=nn.ReLU,
			use_softmax=True):
		super().__init__()

		self.pre = nn.Linear(in_features, hidden_features)

		hidden = [
			nn.Sequential(
				nn.Linear(hidden_features, hidden_features),
				non_linearity(),
			)
			for _ in range(hidden_layers)
		]
		self.hidden = nn.Sequential(*hidden)

		self.post = nn.Sequential(
			nn.Linear(hidden_features, out_features),
			nn.Softmax() if use_softmax else nn.Identity()
		)
	
	def forward(self, x):
		x = self.pre(x)
		x = self.hidden(x)
		x = self.post(x)
		return x
