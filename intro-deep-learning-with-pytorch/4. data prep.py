TensorDataset(tensor(X).float(), tensor(y).float())
dataset[0] # features, target
DataLoader(dataset, batch_size=4, shuffle=True)