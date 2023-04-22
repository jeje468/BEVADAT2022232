import numpy as np
from sklearn.model_selection import train_test_split


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        self.m = 0
        self.c = 0

    def fit(self, X: np.array, y: np.array):
        self.X = X
        self.y = y
    
    def predict(self, X):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        n = float(len(self.X_train))

        losses = []
        for i in range(self.epochs): 
            y_pred = self.m*self.X_train + self.c

            residuals = y_pred - self.y_train
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(self.X_train * residuals)
            D_c = (-2/n) * sum(residuals)
            self.m = self.m + self.lr * D_m
            self.c = self.c + self.lr * D_c


        return self.m*X + self.c
        

