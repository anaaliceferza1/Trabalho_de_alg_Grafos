import networkx as nx
import matplotlib
import numpy as np

from agents.Cops import Cops
from agents.Robbers import Robber
from agents.Ports import Port

from movement_algorithms.bellman_ford import bellman_ford

matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt

class Dgraphs:
    def __init__(self):
        self.graph = nx.DiGraph()

        self.thief = None
        self.police = None
        self.ports = None
        self.thief_log =[]
        self.police_log =[]

        self.loser = False
        self.winner = False
        self.steps = 0

    def create_graphs(self):
        while True:
            try:
                nodes = input("Digite os vértices(n) separados por vírgula: ").split(",")
                if len(nodes)<6:
                    print("O número de vértices deve ser pelo menos 6 para acomodar os portos.")
                    continue
                self.graph.add_nodes_from([n.strip() for n in nodes])
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite novamente.")

        for node in self.graph.nodes():
            altitude = int(input(f"Digite a altitude do vértice(n) {node}: "))
            self.graph.nodes[node]['altitude'] = altitude

        m = int(input("Digite quantidade de arestas(m): "))
        for _ in range(m):
            origin, destine = input("Origem->Destino: ").split("->")
            self.graph.add_edge(origin.strip(), destine.strip())
  
        self.weight_graph()
        self.add_agents()
    
    def add_agents(self):

        if not self.graph.nodes():
            raise ValueError("O grafo deve conter vértices para adicionar os agentes.")

        self.thief = Robber(graph=self.graph)
        self.police = Cops(graph=self.graph)
        self.ports = Port(graph=self.graph)

        self.thief.starting_position()
        
        ports_nodes = self.ports.position()
        entrey_degree = self.ports.entry_degree()

        while True:
            try:
                num_cops = int(input("Digite o número de policiais: "))
                self.police.number_of_cops(self.graph, num_cops, entrey_degree)
                break
            except ValueError as e:
                print(e)

        self.thief_log.append(self.thief.position)
        for p in self.police.positions:
            self.police_log.append([p])

    def ver_agents_nodes(self):
        for node in self.graph.nodes():
            if node in self.police:
                self.graph.nodes()[node]['agent'] = 'police'
            elif node == self.thief:
                self.graph.nodes()[node]['agent'] = 'thief'
            else:
                self.graph.nodes()[node]['agent'] = None

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
    
    def report_example(self):
        '''
        Destinado ao relatorio do jogo
        Qualquer ideia ir adicionando...

        '''
        print("-x-x-x-x--Relatorio--x-x-x-x-")
        if self.winner:
            print("->A fulga foi um sucesso !!!")
        elif self.loser:
            print("-> O ladrao foi pego...")
        else:
            print("Fim de Simulação")
        
        print("Caminho percorrido pelo bandido: ")
        print("".join(self.thief_log ))

        print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")

              
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
