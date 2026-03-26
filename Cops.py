import networkx as nx
from Create_graphos import Dgraphs

class Cops:
    def __init__(self, name):
        self.name = name

    def arrest(self, suspect):
        print(f"{self.name} has arrested {suspect}.")

    def patrol(self):
        print(f"{self.name} is patrolling the area.")
    
    def cops_quantity(self, number):
        print(f"{self.name} has {number} officers on duty.")

    def number_of_cops(self, graph):
        #definir a quantidade de policias com base na quantidade de vértices do grafo
        num_cops = len(graph.graph.nodes()) // 2  # Exemplo: 1 policial para cada 2 vértices
        self.cops_quantity(num_cops)