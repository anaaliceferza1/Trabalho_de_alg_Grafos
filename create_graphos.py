import networkx as nx
import matplotlib
matplotlib.use('TkAgg')  # ou 'Qt5Agg'

import matplotlib.pyplot as plt

class Graphs:
    def __init__(self):
        self.grafo = nx.Graph()

    def create_graphs(self):
        n = int(input("Quantos nós tem o grafo? "))

        for _ in range(n):
            no = input("Nome do nó: ")
            self.grafo.add_node(no)

        m = int(input("Quantas arestas? "))

        for _ in range(m):
            origin = input("Origem: ")
            destine = input("Destino: ")
            self.grafo.add_edge(origin, destine)

    def show_graphs(self):
        plt.figure()
        nx.draw(self.grafo, with_labels=True)
        plt.savefig("grafo.png")