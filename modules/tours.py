import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

def clustering(X: np.ndarray) -> np.ndarray:
    """クラスタリング. k-means?"""
    k = int(X.shape[0]/8)
    X_size,n_features = X.shape
    centroids  = X[np.random.choice(X_size,k)]
    new_centroids = np.zeros((k, n_features))
    cluster = np.zeros(X_size)
    for epoch in range(350):
        for i in range(X_size):
            distances = np.sum((centroids - X[i]) ** 2, axis=1)
            cluster[i] = np.argsort(distances)[0]
        for j in range(k):
            new_centroids[j] = X[cluster==j].mean(axis=0)
        if np.sum(new_centroids == centroids) == k:
            print("break")
            break
        centroids =  new_centroids
    return cluster

def pca(data: np.ndarray) -> np.ndarray:
    """次元削減"""
    pca=PCA(n_components=2)
    data=pca.fit_transform(data)
    return data

def normalize(X: np.ndarray) -> np.ndarray:
    return MinMaxScaler((0, 100)).fit_transform(X)