import networkx as nx
from graph.Create_graphos import Dgraphs
from agents.Robbers import Robber
from agents.Ports import Port

import math

class Cops:
    def __init__(self, name = None, graph = None):
        self.graph = graph
        self.ports = Port()

    def arrest(self, suspect):
        print(f"{self.name} prendeu {suspect}.")

    def patrol(self):
        print(f"{self.name} estah patrulhando a area.")
    
    def cops_quantity(self, number):
        print(f"{self.name} has {number} estao patrulhando.")

    def number_of_cops(self, number, entrey_degree):
        cops_needes = number
        if cops_needes > entrey_degree:
            raise ValueError(f"Numero de policiais necessarios ({cops_needes}) nao pode ser maior que: {entrey_degree}.")
        else:
            print(f"Numero de policiais necessarios: {cops_needes}.")
