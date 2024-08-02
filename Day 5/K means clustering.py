import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
X,y=make_blobs(n_samples=300,centers=4,cluster_std=0.6,random_state=0)
plt.scatter(X[:,0],X[:,1],s=50)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Synthetic data for K-means clustering")
plt.show()
kmeans=KMeans(n_clusters=4,random_state=0)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],c=y_kmeans,s=50,cmap='viridis')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Synthetic data for K-means clustering")
plt.show()
sil_score=silhouette_score(X,y_kmeans)
print(f'Silhouette score: {sil_score:.2f}')