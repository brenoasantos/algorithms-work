import PySimpleGUI as sg
from kruskal import Graph
from pandas import read_csv

url_nodes = 'https://raw.githubusercontent.com/mathbeveridge/asoiaf/master/data/asoiaf-all-nodes.csv'
url_edges = 'https://raw.githubusercontent.com/mathbeveridge/asoiaf/master/data/asoiaf-all-edges.csv'

nodes = read_csv(url_nodes)
edges= read_csv(url_edges)



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
x = (result['minimum'])

#----------------Interface gráfica do usuário----------------#
class AlgorithmScreen:
    def __init__(self):
        layout = [
            [sg.Text('Kruskal Algorithm - GOT Characters', justification='center', size=(50,0))],
            [sg.Text((f'Minimum Connections: {x}'), justification='center', size=(50,0))],
            [sg.Text('Close window to see the magic', justification='center', size=(50,0))],

        ]
        screen = sg.Window(title= 'GOT Character Connections', size = (400, 100)).layout(layout)
        self.button, self.values = screen.Read()

    def start(self):
        print(self.values)

window = AlgorithmScreen()
window.start()
