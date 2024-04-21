import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import Birch

# Load the dataset
data = pd.read_csv('birch_dataset.csv')

# Visualize the data
plt.scatter(data['X'], data['Y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Birch Clustering Data')
plt.show()

# Perform Birch clustering
birch = Birch(n_clusters=2, threshold=0.5)
birch.fit(data)

# Get the cluster labels
labels = birch.labels_

# Visualize the clusters
plt.scatter(data['X'], data['Y'], c=labels, cmap='viridis')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Birch Clustering')
plt.show()
