import networkx as nx
from graph.Create_graphos import Dgraphs
from agents.Robbers import Robber
from agents.Ports import Port

import math

class Cops:
    def __init__(self, name = None, graph = None):
        self.graph = graph
        self.positions = []
        self.ports = Port()

    def arrest(self, suspect):
        print(f"{self.name} prendeu {suspect}.")

    def patrol(self):
        print(f"{self.name} estah patrulhando a area.")
    
    def cops_quantity(self, number):
        print(f"{self.name} has {number} estao patrulhando.")

    def number_of_cops(self, number, entrey_degree):
        cops_needes = number

        n = len(self.graph.nodes())
        floor = math.isqrt(n)
        roof = entrey_degree

        if cops_needes <= floor:
            raise ValueError(f"Numero de equipe de policiais necessarios ({cops_needes}) nao pode ser menor ou igual a: {floor}.")
        elif cops_needes > roof:
            raise ValueError(f"Numero de equipe de policiais necessarios ({cops_needes}) nao pode ser maior que: {roof}.")
        else:
            print(f"Numero de equipe de policiais necessarios: {cops_needes}.")
        #Aqui vai posicionar os policiais de forma aleatoria

        nodes = list(self.graph.nodes())
        self.positions = nodes[:number]

        for c in self.positions:
            self.graph.nodes[c]['agent'] = 'police'

        