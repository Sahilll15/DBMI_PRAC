import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('clique_dataset.csv')

# Create a graph
G = nx.Graph()

# Add edges to the graph
for index, row in data.iterrows():
    G.add_edge(row['Node1'], row['Node2'])

# Detect cliques
cliques = list(nx.find_cliques(G))

# Print the cliques
print("Cliques found:")
for clique in cliques:
    print(clique)

# Draw the graph with cliques highlighted
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1500)
for clique in cliques:
    nx.draw_networkx_nodes(G, pos, nodelist=clique, node_color='orange', node_size=1500)
plt.title('Clique Clustering')
plt.show()
