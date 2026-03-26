import networkx as nx
import matplotlib
import numpy as np
matplotlib.use('TkAgg')  # ou 'Qt5Agg'

import matplotlib.pyplot as plt
#pip3 install networkx matplotlib numpy

class Dgraphs:
    def __init__(self):
        self.graph = nx.DiGraph()

        self.thief = None
        self.police = []

        self.loser = False
        self.winner = False
        self. step = 0

    def create_graphs(self):
        nodes = input("Digite os vértices(n) separados por vírgula: ").split(",")
        self.graph.add_nodes_from([n.strip() for n in nodes])

        for node in self.graph.nodes():
            altitude = int(input(f"Digite a altitude do vértice(n) {node}: "))
            self.graph.nodes()[node]['altitude'] = altitude

        m = int(input("Quantas arestas(m)? "))
        for _ in range(m):
            origin, destine = input("Origem->Destino: ").split("->")
            self.graph.add_edge(origin.strip(), destine.strip())

    def weight_graph(self):
        for v in self.graph.nodes():
            for u in self.graph.successors(v):
                if v != u:
                    edge = (v, u)
                    diff = self.graph.nodes()[u]['altitude'] - self.graph.nodes()[v]['altitude']
                    if diff > 0:
                        w = diff*2
                        self.graph.edges[edge]['weight'] = w
                    else:
                        w = diff/2
                        self.graph.edges[edge]['weight'] = w
        
        self.killing_negative_cycles()

# Removi a ultima função e adicionei a versão (apenas de verificação) junto com o Bellman pq fica mais otimizado :C
    def bellman_ford(self, source):
        dist = {v: float('inf') for v in self.graph.nodes()}
        prev = {v: None for v in self.graph.nodes()}

        dist[source] = 0

        for _ in range(len(self.graph.nodes())-1):
            updated = False
            for u,v,data in self.graph.edges(data=True):
                if 'weight' not in data: 
                    print("Aresta sem peso", u, v)

                w = data['weight']
                if (dist[u] + w) < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
            if not updated:
                break
        for u,v,data in self.graph.edges(data=True):
            w = data['weight']
            if dist[u] + w < dist[v]:
                return dist,prev,(u,v)
        
        return dist, prev, None
    
    def killing_negative_cycles(self):
        '''
        So remove os ciclos negativos encontrados pelo algoritmo do Bellzinho

        '''
        while True:
            dist, prev,cycle_edge =  self.bellman_ford(next(iter(self.graph.nodes())))
            if not cycle_edge:
                break
            else:
                self.graph.remove_edge(*cycle_edge)

    def draw_graphs(self):
        pos = nx.spring_layout(self.graph, seed=42)
        
        labels = {node:f"{node}\n{self.graph.nodes()[node]['altitude']}m" for node in self.graph.nodes()}
        
        edge_labels = {(u, v):f"{d['weight']:.1f}" for u, v, d in self.graph.edges(data=True)}
        
        node_colors = ["orange" if self.graph.nodes()[node]['altitude'] == max(nx.get_node_attributes(self.graph, 'altitude').values()) else "lightblue" for node in self.graph.nodes()]
        
        nx.draw(self.graph, pos, with_labels=False, node_color=node_colors, node_size=1500, arrowsize=True)
        nx.draw_networkx_labels(self.graph, pos, labels=labels)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title("Ilha e seus locais")
        plt.show()

    def show_graph(self):
        print("\nGrafo:")
        for no in self.graph.nodes():
            neigh = list(self.graph.successors(no)) 
            print(f"{no} -> Vizinhos: {neigh}")
