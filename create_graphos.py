import networkx as nx
import matplotlib
matplotlib.use('TkAgg')  # ou 'Qt5Agg'

import matplotlib.pyplot as plt

class Diagraphs:
    def __init__(self):
        self.graph = nx.DiGraph()

    def create_graphs(self):
        nodes = input("Digite os nós separados por vírgula: ").split(",")
        self.graph.add_nodes_from([n.strip() for n in nodes])

        m = int(input("Quantas arestas? "))
        for _ in range(m):
            origin, destine = input("Origem->Destino: ").split("->")
            self.graph.add_edge(origin.strip(), destine.strip())

    def weight_graph(self):
        for edge in self.graph.edges():
            weight = int(input(f"Peso da aresta {edge}: "))
            self.graph[edge[0]][edge[1]]['weight'] = weight
    
    def show_graphs_png(self):
        plt.figure()
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color="lightblue", edge_color="gray")
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()

    def show_graph(self):
        print("\nGrafo:")
        for no in self.graph.nodes():
            exit_degree = list(self.graph.successors(no)) 
            entry_degree = list(self.graph.predecessors(no))
            print(f"{no} -> Sair: {exit_degree}, Entrar: {entry_degree}")
