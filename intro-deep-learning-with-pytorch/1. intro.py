import torch
from torch import nn

x = torch.tensor([1,2,3,4]).float()

model = nn.Sequential(
    nn.Linear(4, 2),
    nn.Linear(2, 1),
    nn.Sigmoid()
)

print(model(x))