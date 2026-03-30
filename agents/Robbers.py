from platform import node
from movement_algorithms.bellman_ford import Bellman_ford
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
        bf = Bellman_ford(self.graph)

        distances, predecessors, _ = bf.alg_bellman_ford(self.position) #ok

        if distances is None or predecessors is None:
            print("Não foi possível calcular os caminhos mais curtos.")
            return
        
        ports = [
            port for port in self.graph.nodes() 
            if self.graph.nodes[port].get('agent')=='port' 
            and distances.get(port, float('inf')) != float('inf')
        ]

        if not ports:
            print("Não há portos disponíveis para o ladrão se mover.")
            return

        paths_sorted = sorted(ports, key=lambda p: distances[p])

        for port in paths_sorted:
            path = bf.reconstruct_paths(predecessors, self.position, port)
            
            if not path or len(path) <= 1:
                continue  

            next_move = path[1] 
            
            if self.graph.nodes[next_move].get('agent') == 'police':
                print(f"Caminho para o {port} esta bloqueado.\nO ladrao encontrou um policial em {next_move} e precisa escolher outro caminho.")
                continue
            self.graph.nodes[self.position].pop('agent', None)
            self.position = next_move
            self.graph.nodes[self.position]['agent'] = 'thief'

            print(f"O ladrao se moveu para {next_move}.")

            return self.position
            
        print("Todos os caminhos estão bloqueados. O ladrão perdeu")
        return None



        

        

