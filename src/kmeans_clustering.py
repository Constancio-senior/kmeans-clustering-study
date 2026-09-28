import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
plt.style.use("dark_background")

X, Y = make_blobs(n_samples=100,centers=3, random_state=42)
modelo= KMeans(n_clusters=3,n_init=10, random_state=42)
modelo.fit(X)
print("KMEANS OK")
print(modelo.inertia_)
print(modelo.cluster_centers_)
print(silhouette_score(X,modelo.labels_))

plt.figure(figsize=(8, 6))

plt.scatter(X[:, 0], X[:, 1],c=modelo.labels_,cmap="viridis",s=60)

plt.scatter(modelo.cluster_centers_[:, 0],modelo.cluster_centers_[:, 1], c="red", marker="X", s=220, label="Centroides")

plt.title("K-Means Clustering - 3 Clusters")
plt.xlabel("Feature X1")
plt.ylabel("Feature X2")
plt.grid(True, alpha=0.3)
plt.legend()

plt.savefig(__file__.replace("kmeans_clustering.py","kmeans_clustering.png))
plt.close()
