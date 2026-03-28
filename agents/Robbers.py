from platform import node

from graph.Create_graphos import Dgraphs

from agents.Cops import Cops
from agents.Ports import Port
from movement_algorithms.bellman_ford import bellman_ford
from movement_algorithms.bellman_ford import reconstruct_paths

import networkx as nx   

class Robber:
    def __init__(self, graph = None):
        self.graph = graph
        self.position = None
    
    #ja que agora vai ser passado
    def starting_position(self, start_node):
        self.position = start_node
        self.graph.nodes[start_node]['agent'] = 'thief'
    
    def steal(self):
        print("O ladrao esta roubando!")

    def move(self):
        distances, predecessors = bellman_ford(self.graph, self.position)

        if distances is None or predecessors is None:
            print("Não foi possível calcular os caminhos mais curtos.")
            return
        
        ports = [port for port in self.graph.nodes() 
                 if self.graph.nodes[port].get('agent')=='port' and distances[port] != float('inf')]
        
        if not ports:
            print("Não há portos disponíveis para o ladrão se mover.")
            return

        paths_sorted = sorted(ports, key=lambda p: distances[p])

        for port in paths_sorted:
            path = reconstruct_path(predecessors, self.position, port)
            
            if len(path) <= 1:
                continue

            next_move = path[1] 
            
            if self.graph.nodes[next_move].get('agent') == 'police':
                print(f"Caminho para o {port} esta bloqueado.\nO ladrao encontrou um policial em {next_move} e precisa escolher outro caminho.")
            else:
                print(f"O ladrao se moveu para {next_move}.")
                self.position = next_move

                return self.position
            
        print("Todos os caminhos estão bloqueados. O ladrão perdeu")
        return None



        

        

