import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim

x = torch.tensor([1,2,3,4]).float()
y = [2]
sample_pred = torch.tensor([[0.1, 6.0, -2.0, 3.2]])

one_hot_label = F.one_hot(torch.tensor(y), num_classes=sample_pred.shape[1])
crit = nn.CrossEntropyLoss()
loss = crit(sample_pred.double(), one_hot_label.double())

model = nn.Sequential(
    nn.Linear(4, 2),
    nn.Linear(2, 3),
    nn.Linear(3, 1),
    nn.Softmax()
)

preds = model(x)

crit = nn.CrossEntropyLoss()
loss = crit(preds, y)
loss.backward()

optimizer = optim.SGD(model.parameters(), lr=0.001)
loss = crit(pred, target)
loss.backward()
optimizer.step()


for i in range(num_epochs):
  for data in dataloader:
    optimizer.zero_grad()
    feature, target = data
    prediction = model(feature)  
    loss = criterion(prediction, target)   
    loss.backward()
    optimizer.step()
show_results(model, dataloader)