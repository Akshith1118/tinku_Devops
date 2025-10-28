import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
df = pd.read_csv("C:\ML programs\clusterdata.csv")
print(df.head())
X = df[['Distance_Feature', 'Speeding_Feature']].values
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.scatter(X[:,0], X[:,1], c='blue')
plt.title("Raw Dataset")
plt.xlabel("Distance Feature")
plt.ylabel("Speeding Feature")
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
labels_k = kmeans.labels_
plt.subplot(1,3,2)
plt.scatter(X[:,0], X[:,1], c=labels_k, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],s=200, c='red', marker='X')
plt.title("K-Means Clustering")
plt.xlabel("Distance Feature")
plt.ylabel("Speeding Feature")
gmm = GaussianMixture(n_components=3, random_state=0).fit(X)
labels_g = gmm.predict(X)
plt.subplot(1,3,3)
plt.scatter(X[:,0], X[:,1], c=labels_g, cmap='plasma')
plt.title("Gaussian Mixture Model")
plt.xlabel("Distance Feature")
plt.ylabel("Speeding Feature")
plt.tight_layout()
plt.show()
