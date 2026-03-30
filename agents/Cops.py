import networkx as nx
import math
import random
from movement_algorithms.bellman_ford import Bellman_ford

class Cops:
    def __init__(self, graph = None):
        self.graph = graph
        self.positions = []

        self.police_team = None

    def add_position(self, pos):
        self.positions.append(pos)


    def arrest(self, suspect):
        print(f"{self.name} prendeu {suspect}.")

    def patrol(self):
        print(f"{self.name} estah patrulhando a area.")
    
    def cops_quantity(self, number):
        print(f"{self.name} has {number} estao patrulhando.")

    def number_of_cops(self, number, entrey_degree):
        cops_needes = number
        #agora so vai validar a quantidade de policiais com base no grau de entrada dos portos e na quantidade de nós do grafo
        n = len(self.graph.nodes())
        floor = math.isqrt(n)
        roof = entrey_degree

        if cops_needes <= floor:
            raise ValueError(f"Numero de equipe de policiais necessarios ({cops_needes}) nao pode ser menor ou igual a: {floor}.")
        elif cops_needes > roof:
            raise ValueError(f"Numero de equipe de policiais necessarios ({cops_needes}) nao pode ser maior que: {roof}.")
        else:
            print(f"Numero de equipe de policiais necessarios: {cops_needes}.")
        
    #pra salvar oque foi passado no arquivo
    def set_positions(self, positions):
        self.positions = positions

        nodes = list(self.graph.nodes())
        self.positions = nodes[:number]

        for c in self.positions:
            self.graph.nodes[c]['agent'] = 'police'

    def move(self, thief_pos, persecution):

        bf = Bellman_ford(self.graph)

        for i, cop_pos in enumerate(self.positions):
            
            next_move = cop_pos  # default 

            #caso roubo ainda nao tiver acontecido
            if not persecution:
                
                neighbor = list(self.graph.neighbors(cop_pos)) + list(self.graph.predecessors(cop_pos))

                random_neighbor = random.choice(neighbor)

                next_move = random_neighbor

            #se tiver em perseguiçao
            else:
                distances, predecessors = bf.alg_bellman_ford(self.graph, cop_pos)

                if distances is None or predecessors is None:
                    continue

                path = bf.reconstruct_paths(predecessors, cop_pos, thief_pos)

                if not path or len(path) < 2:
                    continue

                if persecution == True:
                    if len(path) > 2:
                        next_move = path[2]  
                    else:
                        next_move = path[1]  

            #atualiza grafo
            self.graph.nodes[cop_pos]['agent'] = ''
            self.positions[i] = next_move
            self.graph.nodes[next_move]['agent'] = 'police'
        
       

        



            


            



        
            



    '''
        def police_vehicle():
            print("viatura criada")
    '''
        