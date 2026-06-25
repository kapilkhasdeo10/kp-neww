import numpy as np

def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x): return x * (1 - x)

#XOR problem dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])

np.random.seed(42)
W1 = np.random.rand(2, 4) * 0.5  #input hidden layer weights
W2 = np.random.rand(4, 1) * 0.5  #hidden output layer weights

lr = 0.5  #learning rate
losses = []

for epoch in range(10000):
    #forward pass
    h = sigmoid(X @ W1)  
    o = sigmoid(h @ W2)
    
    #loss calculation
    loss = np.mean((Y - o) ** 2)
    losses.append(loss)
    
    #backward pass
    d_o = (o - Y) * sigmoid_derivative(o)
    d_h = (d_o @ W2.T) * sigmoid_derivative(h)
    
    #update weights
    W2 -= lr * h.T @ d_o
    W1 -= lr * X.T @ d_h

import matplotlib.pyplot as plt
plt.plot(losses)
plt.title('Loss decreasing during training')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()

print('Final predictions (should be close to [0, 1, 1, 0]):')
print(np.round(o, 2))