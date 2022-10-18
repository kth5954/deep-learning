import numpy as np

x = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])
y = np.dot(x, W)
print(W.shape)
print(y)