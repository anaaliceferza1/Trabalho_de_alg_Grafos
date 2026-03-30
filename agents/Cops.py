from movement_algorithms.bellman_ford import Bellman_ford 
import networkx as nx
import random
import math


class Cops:
    def __init__(self, graph = None):
        self.graph = graph
        self.positions = []
        self.police_team = None

    def arrest(self, suspect):
        print(f"{self.name} prendeu {suspect}.")

    def patrol(self):
        print(f"{self.name} estah patrulhando a area.")
    
    def cops_quantity(self, number):
        print(f"{self.name} has {number} estao patrulhando.")

    def number_of_cops_valid(self, number, entrey_degree):
        cops_needes = number
        #agora so vai validar a quantidade de policiais com base no grau de entrada dos portos e na quantidade de nós do grafo
        n = len(self.graph.nodes())
        floor = math.isqrt(n)
        roof = entrey_degree

        if cops_needes > roof:
            raise ValueError(f"Numero de equipe de policiais necessarios ({cops_needes}) nao pode ser maior que: {roof}.")
        else:
            self.police_team = cops_needes
            print(f"Numero de equipe de policiais necessarios: {cops_needes}.")
        
    #pra salvar oque foi passado no arquivo
    def set_positions(self, positions):
        self.positions = list(positions)

        for c in self.positions:
            self.graph.nodes[c]['agent'] = 'police'

    #movimentacao tanto em patrulha quanto perseguicao
    def move(self, thief_pos, persecution):
        bf = Bellman_ford(self.graph)
        new_positions = []

        for cop_pos in self.positions:
            next_move = cop_pos  # default 

            #caso roubo ainda nao tiver acontecido
            if not persecution:
                neighbor = list(self.graph.neighbors(cop_pos)) + list(self.graph.predecessors(cop_pos))
                
                if neighbor:
                    random_neighbor = random.choice(neighbor)
                    next_move = random_neighbor

            #se tiver em perseguiçao
            else:
                distances, predecessors, _ = bf.alg_bellman_ford(cop_pos)
                path = None

                if distances is not None and predecessors is not None:
                    path = bf.reconstruct_paths(predecessors, cop_pos, thief_pos)
                
                if path and len(path)>1:
                    step1 = path[1]

                    if step1 == thief_pos:
                        next_move = step1
                    elif len(path) > 2:
                        next_move = path[2]
                    else:
                        next_move = step1

            new_positions.append(next_move)

        '''
        Atualiza as posicoes antigas
        dps atualiza a lista das novas posicoes 
        por fim atualiza as novas posicoes
        '''
        #self.graph.nodes[cop_pos]['agent'] = ''
        for pos in self.positions:
            if self.graph.nodes[pos].get('agent') == 'police':
                del self.graph.nodes[pos]['agent']

        self.positions = new_positions
        
        for pos in self.positions:
            self.graph.nodes[pos]['agent'] = 'police'



        



            


            



        
            



    '''
        def police_vehicle():
            print("viatura criada")
    '''
        