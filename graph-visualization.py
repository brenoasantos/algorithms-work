from kruskal import Graph
from gui import AlgorithmScreen
import networkx as nx
import matplotlib.pyplot as plt
from pandas import read_csv

window = AlgorithmScreen()
window.start()

url_nodes = 'https://raw.githubusercontent.com/mathbeveridge/asoiaf/master/data/asoiaf-all-nodes.csv'
url_edges = 'https://raw.githubusercontent.com/mathbeveridge/asoiaf/master/data/asoiaf-all-edges.csv'

nodes = read_csv(url_nodes)
edges= read_csv(url_edges)

file = open('./database/nodes.txt')
all_lines = file.readlines()

graph = nx.Graph()
#ADD NODES(VERTEX)
for line in all_lines:
  graph.add_node(line.split(',')[0])

namesAndId = []
for index, row in nodes.iterrows():
  namesAndId.append(index)
  namesAndId.append(row[0])

g = Graph(796)
for index, row in edges.iterrows():
  indexFirstName = namesAndId.index(row[0])
  indexSecondName = namesAndId.index(row[1])
  g.addEdge(namesAndId[indexFirstName-1], namesAndId[indexFirstName], namesAndId[indexSecondName-1], namesAndId[indexSecondName], row[4])

result = g.Kruskal()
kruskal_tree = result['kruskalResult']

for i in range(len(kruskal_tree)):
  origin_name = (kruskal_tree[i][1])
  destiny_name = (kruskal_tree[i][3])
  weight = (kruskal_tree[i][4])
  graph.add_edge(origin_name, destiny_name, weight = weight)
  
nx.draw(graph, with_labels=1)
plt.show()
