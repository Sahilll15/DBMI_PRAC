import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('kmeans_dataset.csv')

# Visualize the data
plt.scatter(data['X'], data['Y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('KMeans Data')
plt.show()

# Perform KMeans clustering
k = 2  # Number of clusters
kmeans = KMeans(n_clusters=k)
kmeans.fit(data)

# Get the cluster centers and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Visualize the clusters
colors = ['r', 'g', 'b', 'y']  # Define colors for each cluster (up to 4 clusters)
for i in range(k):
    plt.scatter(data.loc[labels == i, 'X'], data.loc[labels == i, 'Y'], c=colors[i], label='Cluster {}'.format(i+1))
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=300, c='black', label='Centroids')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('KMeans Clustering')
plt.legend()
plt.show()
