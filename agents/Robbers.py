from sys import path

from graph.Create_graphos import Dgraphs

from agents.Cops import Cops
from agents.Ports import Port
from movement_algorithms.bellman_ford import bellman_ford

import networkx as nx   

class Robber:
    def __init__(self, graph = None):
        self.graph = graph
        self.castale = None
    
    def steal(self):
        print("O ladrao esta roubando!")
        

        

