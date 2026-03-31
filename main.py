from graph.Create_graphos import Dgraphs

from Game import Game

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



file_name = input("Insira o nome do seu arquivo(com '.txt'): ")
print("Pasta atual:", os.getcwd())
print("Arquivo existe?", os.path.exists(file_name))

try:
    g = Dgraphs()
    g.create_graphs(file_name)
    g.draw_graphs()
    g.show_graph()
    game = Game()
    game.game_simulation(g)
    game.report_example(g)
    

except FileNotFoundError:
    print("!Arquivo não encontrado!")
except Exception as e:
    print("!Erro ao processar arquivo:", e , "!")



