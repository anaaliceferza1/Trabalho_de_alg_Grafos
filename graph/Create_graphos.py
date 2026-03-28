import networkx as nx
import matplotlib
import numpy as np

from agents.Cops import Cops
from agents.Robbers import Robber
from agents.Ports import Port

matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
    
def ver_qtd_polices(qtd_polices):
    if qtd_polices <= 0:
        raise ValueError("Número de police_positions deve ser positivo.")  


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

    def create_graphs(self, file_name):

        with open(file_name, "r", encoding="utf-8") as f:
            row = [l.strip() for l in f if l.strip()]
        
        #a quantidade de vertices e arestar
        n = int(row[0])
        m = int(row[1])

        edges = []
        nodes = set()

        #vai pegar as as linhas das arestas e seus pesos
        for i in range(2, 2 + m):
            u, v, w = row[i].split()
            w = int(w)

            edges.append((u, v, w))
            nodes.add(u)
            nodes.add(v)
        
        #vai adicionar os nós
        self.graph.add_nodes_from(nodes)

        #adiciona as arestas
        for u, v, w in edges:
            self.graph.add_edge(u, v, weight=w)

        self.thief_start = row[2 + m]
        self.ports_nodes = row[3 + m].split()

        qtd_polices = int(row[4 + m])
        police_positions = row[5 + m].split()

        if qtd_polices != len(police_positions):
            raise ValueError("Quantidade de police_positions inconsistente.")

        self.weight_graph()
        self.initialize_agents(qtd_polices, police_positions)

    
    def initialize_agents(self, qtd_polices, police_positions ):

        ver_qtd_polices(qtd_polices)

        self.thief = Robber(graph=self.graph)
        self.police = Cops(graph=self.graph)
        self.ports = Port(graph=self.graph)

        self.thief.starting_position(self.thief_start)
        self.ports.position(self.ports_nodes)
        self.police.set_positions(police_positions)
        
        entry_degree = self.ports.entry_degree()

        while True:
            try:
                self.police.number_of_cops(self.graph, qtd_polices, entry_degree)
                break
            except ValueError as e:
                try:
                    qtd_polices = int(input("Digite um novo número de police_positions: "))
                    ver_qtd_polices(qtd_polices) 
                except ValueError:
                    print("Digite apenas números!")


        self.thief_log.append(self.thief.castle)
        self.police_log.extend(self.police.positions)


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

# Removi a ultima função e adicionei a versão (apenas de verificação) junto com o Bellman pq fica mais otimizado :C
    
    
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

    def report_example(self):
        '''
        Destinado ao relatorio do jogo
        Qualquer ideia ir adicionando...

        '''
        print("-x-x-x-x--Relatorio--x-x-x-x-")
        if self.winner:
            print("->A fulga foi um sucesso !!!")
        else:
            print("-> O ladrao foi pego...")
        



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
            