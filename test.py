import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()
graph.add_node('breno')
graph.add_node('luca')

graph.add_edge('breno', 'luca', weight=3)

nx.draw(graph, with_labels=2)
plt.show()