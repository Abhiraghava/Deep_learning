# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-fks0143PPfTvuE3NHPtoVTmTWBFlyv8
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(0)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class SigmoidNeuron:
    def __init__(self):
        self.weights = None
        self.bias = None

    def train(self, X, y, learning_rate=0.01, epochs=1000):
        n_samples, n_features = X.shape

        self.weights = np.random.rand(n_features)
        self.bias = np.random.rand()

        for _ in range(epochs):
            linear_output = np.dot(X, self.weights) + self.bias
            predictions = sigmoid(linear_output)

            dw = (1 / n_samples) * np.dot(X.T, (predictions - y))
            db = (1 / n_samples) * np.sum(predictions - y)

            self.weights -= learning_rate * dw
            self.bias -= learning_rate * db

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        predictions = sigmoid(linear_output)
        return (predictions > 0.5).astype(int)

model = SigmoidNeuron()
model.train(X_train, y_train, learning_rate=0.1, epochs=1000)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")