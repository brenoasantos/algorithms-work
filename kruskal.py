from pandas import read_csv

url_nodes = 'https://raw.githubusercontent.com/mathbeveridge/asoiaf/master/data/asoiaf-all-nodes.csv'
url_edges = 'https://raw.githubusercontent.com/mathbeveridge/asoiaf/master/data/asoiaf-all-edges.csv'

nodes = read_csv(url_nodes)
edges= read_csv(url_edges)

class Graph:
    def __init__(self, vertices):
        self.graph = []
        self.numOfVertices = vertices 
 
    def addEdge(self, origin, originName, destiny, destinyName, weight):
        self.graph.append([origin, originName, destiny, destinyName, weight])
 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    def union(self, parent, rank, safeOrigin, safeDestiny):
        safeOriginRoot = self.find(parent, safeOrigin)
        safeDestinyRoot = self.find(parent, safeDestiny)
 
        if rank[safeOriginRoot] < rank[safeDestinyRoot]:
            parent[safeOriginRoot] = safeDestinyRoot
        elif rank[safeOriginRoot] > rank[safeDestinyRoot]:
            parent[safeDestinyRoot] = safeOriginRoot
        else:
            parent[safeDestinyRoot] = safeOriginRoot
            rank[safeOriginRoot] += 1
 
    def Kruskal(self):
        kruskalResult = []
        indexEdges = 0
        indexResult = 0
 
        # order by lower weight //item[2] == weight
        self.graph = sorted(self.graph, key=lambda item: item[4])
 
        parent = []
        rank = []

        for node in range(self.numOfVertices):
            parent.append(node)
            rank.append(0)
 
        # Until reach all vertices
        while indexResult < self.numOfVertices - 1:
            origin, originName, destiny, destinyName, weight = self.graph[indexEdges]
            indexEdges = indexEdges + 1
            originValueInParent = self.find(parent, origin)
            destinyValueInParent = self.find(parent, destiny)

            # if originParentValue == destinyParentValue there is a cycle, so we cant add this edge (discard it)
            if originValueInParent != destinyValueInParent:
                indexResult = indexResult + 1
                kruskalResult.append([origin,originName, destiny, destinyName, weight]) #including edge that does not cause cycle into result list
                self.union(parent, rank, originValueInParent, destinyValueInParent)
 
        cost = 0
        print("Árvore geradora mínima")
        for origin, originName, destiny, destinyName, weight in kruskalResult:
            cost += weight
            print(originName, '-->', destinyName, 'weight: ', weight)
        print("Somatório dos pesos", cost)
        return {'kruskalResult':kruskalResult, 'minimum':cost}

namesAndId = []
for index, row in nodes.iterrows():
  namesAndId.append(index)
  namesAndId.append(row[0])

g = Graph(796)
for index, row in edges.iterrows():
  indexFirstName = namesAndId.index(row[0])
  indexSecondName = namesAndId.index(row[1])
  g.addEdge(namesAndId[indexFirstName-1], namesAndId[indexFirstName], namesAndId[indexSecondName-1], namesAndId[indexSecondName], row[4])

g.Kruskal()