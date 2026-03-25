import networkx as nx
import matplotlib
import numpy as np
matplotlib.use('TkAgg')  # ou 'Qt5Agg'

import matplotlib.pyplot as plt
#pip3 install networkx matplotlib numpy

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
