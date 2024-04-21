import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Load the dataset
data = pd.read_csv('dbscan_dataset.csv')

# Visualize the data
plt.scatter(data['X'], data['Y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('DBSCAN Data')
plt.show()

# Perform DBSCAN clustering
dbscan = DBSCAN(eps=1, min_samples=2)
dbscan.fit(data)

# Get the cluster labels
labels = dbscan.labels_

# Visualize the clusters
plt.scatter(data['X'], data['Y'], c=labels, cmap='viridis')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('DBSCAN Clustering')
plt.show()
