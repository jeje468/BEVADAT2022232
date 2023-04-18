import numpy as np
from sklearn.model_selection import train_test_split


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        self.m = 0 #meredekség
        self.c = 0 #metszés az x tengellyel

    def fit(self, X: np.array, y: np.array):
        self.X = X
        self.y = y
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.build()

    def build(self):
        # Building the model
        n = float(len(self.X_train)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs): 
            y_pred = self.m*self.X_train + self.c  # The current predicted value of Y

            residuals = y_pred - self.y_train #meghatározzuk a távolságot
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(self.X_train * residuals)  # Derivative wrt m -> mennyivel kell változtatni m-t
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c -> mennyivel kell változtatni c-t
            self.m = self.m + self.lr * D_m  # Update m
            self.c = self.c + self.lr * D_c  # Update c
            if i % 100 == 0:
                print(np.mean(self.y_train-y_pred))
    

    def predict(self, X):
        return self.m*X + self.c

