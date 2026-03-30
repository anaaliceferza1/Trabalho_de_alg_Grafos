from graph.Create_graphos import Dgraphs

from agents.Cops import Cops
from agents.Robbers import Robber
from agents.Ports import Port

from movement_algorithms.bellman_ford import Bellman_ford

import networkx as nx3
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# Número de vértices |V | = n;
# – Número de arestas |E| = m;
# – Lista de arestas no formato: u v w(u, v) (significa aresta entre vértices u e v com peso w(u, v));
# – Vértice que representa o local do roubo;
# – Vértices de saída da ilha, diferentes do local do roubo;
# – Quantidade e posições iniciais das equipes de polícia;


# a estrutura do arquivo.
print("O arquivo tem que esta dentro do mesmo diretorio do main.py:\n")
print("É esperado que o aquivo tenha apenas numeros e nessa configuração:\n")
print("Número de vértices |V| = n")
print("Número de arestas |E| = m")
print("Lista de arestas no formato: u v w(u, v)")
print("Vértice do local do roubo")
print("Vértices de saída da ilha")
print("Quantidade dos policiais\n ")
print("Posiçoes dos policiais\n")


import os

def game_simulation(self):
    '''
        inicializa historico de passos 
        Primeiro o ladrao se move
        Dps o policial se move(entra em perseguição ).
        atualiza historido de passos
        Dps verificamos se o ladrao foi pego ou se escapou.

        '''
    step = 0

    self.thief_log.append(self.thief.position)
    self.police_log.append(list(self.police.positions))

    while True:
        step += 1
        self.steps = step

        thief_move = self.thief.move()

        if thief_move is not None:
            self.graph.nodes[self.thief.position]['agent'] = None
            self.thief.position = thief_move
            self.graph.nodes[thief_move]['agent'] = 'thief'
        
        perseg = True

        self.police.move(self.thief.position, perseg)

        self.thief_log.append(self.thief.position)
        self.police_log.append(list(self.police.positions))
        
        if self.thief.position in self.police.positions:
            self.loser = True
            print("O ladrão foi pego! A polícia venceu!")
            break
        if self.thief.position in self.ports.ports:
            self.winner = True
            print("O ladrão escapou pelos portos! O ladrão venceu!")
            break


file_name = input("Insira o nome do seu arquivo:")
print("Pasta atual:", os.getcwd())
print("Arquivo existe?", os.path.exists("file_name"))

try:
    g = Dgraphs()
    g.create_graphs(file_name)
    g.draw_graphs()
    g.show_graph()

except FileNotFoundError:
    print("!Arquivo não encontrado!")
except Exception as e:
    print("!Erro ao processar arquivo:", e , "!")



