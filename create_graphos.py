import networkx as nx
import matplotlib
import numpy as np
matplotlib.use('TkAgg')  # ou 'Qt5Agg'

import matplotlib.pyplot as plt
#pip3 install networkx matplotlib numpy

class Dgraphs:
    def __init__(self):
        self.graph = nx.DiGraph()

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
        
        self.check_dag()

    def check_dag(self):
        while True:
            nodes = list(self.graph.nodes())
            n = len(nodes)
            if n == 0: break

            adj = nx.to_dict_of_dicts(self.graph)
            c = np.full((n + 1, n + 1), float('inf'))
            c[0, 0] = 0

            idx_to_node = {i+1: node for i, node in enumerate(nodes)}
            node_to_idx = {node: i+1 for i, node in enumerate(nodes)}
            for l in range(1, n + 1):
                for k in range(n + 1):
                    val_min = c[l-1, k]
                    
                    for i in range(n + 1):
                        weight = None
                        if i == 0 and k > 0: 
                            weight = 0
                        elif i > 0 and k > 0:
                            u_name, v_name = idx_to_node[i], idx_to_node[k]
                            if self.graph.has_edge(u_name, v_name):
                                weight = self.graph[u_name][v_name].get('weight', 0)
                        
                        if weight is not None:
                            val_min = min(val_min, c[l-1, i] + weight)
                    
                    c[l, k] = val_min
                    
            cycle_node_idx = None
            for k in range(1, n + 1):
                if c[n, k] != c[n-1, k]:
                    cycle_node_idx = k
                    break
            
            if cycle_node_idx:
                node_name = idx_to_node[cycle_node_idx]
                edge_to_remove = list(self.graph.in_edges(node_name))[0]
                print(f"->Ciclo detectado:'{node_name}'. Removendo {edge_to_remove}")
                self.graph.remove_edge(*edge_to_remove)
            else:
                print("O grafo é um DAG.")
                break
    
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
