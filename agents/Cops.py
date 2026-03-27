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
        print(f"{self.name} has arrested {suspect}.")

    def patrol(self):
        print(f"{self.name} is patrolling the area.")
    
    def cops_quantity(self, number):
        print(f"{self.name} has {number} officers on duty.")

    def number_of_cops(self, graph, number):
        entrey_degree = self.ports.entry_degree()
        cops_needes = number
        if cops_needes > entrey_degree:
            raise ValueError(f"Number of cops needed ({cops_needes}) exceeds the total entry degree of the ports ({entrey_degree}).")
        else:
            print(f"Number of cops needed: {cops_needes}.")
