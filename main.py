from graph.Create_graphos import Dgraphs

from Game import Game

import networkx as nx3
import matplotlib
import numpy as np
import os
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# Número de vértices |V | = n;
# – Número de arestas |E| = m;
# – Lista de arestas no formato: u v w(u, v) (significa aresta entre vértices u e v com peso w(u, v));
# – Vértice que representa o local do roubo;
# – Vértices de saída da ilha, diferentes do local do roubo;
# – Quantidade e posições iniciais das equipes de polícia;


# a estrutura do arquivo.
print("\n" + "-"*40)
print("CONFIGURAÇÃO DO ARQUIVO DE ENTRADA:\n\n")

print("Localização:\nO arquivo tem que esta dentro do mesmo diretorio do main.py:\n")

print("Formato:\nÉ esperado que o aquivo tenha apenas numeros e nessa configuração:\n")

print("1. Número de vértices |V|")
print("2. Número de arestas |E|")
print("3. Lista de arestas: 'u v w'(Origem, Destino, Peso)")
print("4. Vértice do local do roubo (Inicio do ladrão)")
print("5. Vértices de saída da ilha (Portos de Fuga)")
print("6. Quantidade dos policiais ")
print("7. Posiçoes dos policiais")
print("\n" + "-"*40)


# file_name = input("Insira o nome do seu arquivo(com '.txt'): ")
# print("Pasta atual:", os.getcwd())
# print("Arquivo existe?", os.path.exists(file_name))

try:
    g = Dgraphs()
    g.create_graphs("teste.txt")
    g.draw_graphs()
    g.show_graph()

    game = Game()
    game.game_simulation(g)
    # game.report_example(g)
    

except FileNotFoundError:
    print("!Arquivo não encontrado!")
except Exception as e:
    print("!Erro ao processar arquivo:", e , "!")



