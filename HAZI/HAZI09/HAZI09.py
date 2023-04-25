import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix


class KMeansOnDigits:
    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = load_digits()

    def predict(self):
        self.model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.clusters = self.model.fit_predict(self.digits.data)

    def get_labels(self):
        l = np.zeros_like(self.clusters)
        for c in range(self.n_clusters):
            mask = (self.clusters == c)
            target = self.digits.target[mask]
            mode = np.bincount(target).argmax()
            l[mask] = mode
        self.labels = l

    def calc_accuracy(self):
        self.accuracy = round(np.mean(self.labels == self.digits.target), 2)

    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)