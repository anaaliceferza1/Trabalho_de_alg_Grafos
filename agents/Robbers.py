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

        distances, predecessors, _ = bf.alg_bellman_ford(self.position) 

        if distances is None or predecessors is None:
            print("Não foi possível calcular os caminhos mais curtos.")
            return False
        
        ports = [
            port for port in self.graph.nodes() 
            if self.graph.nodes[port].get('agent')=='port' 
            and distances.get(port, float('inf')) != float('inf')
        ]

        if not ports:
            print("Não há portos disponíveis para o ladrão se mover.")
            return False

        #antiga forma nao estava alcancado os caminhos globais e testava todos os nos mesmo bloqueado
        #decidimos alterar para pegar um menor global
        best_option = None

        for port in ports:
            path = bf.reconstruct_paths(predecessors, self.position, port)
            
            if not path or len(path) <= 1:
                continue  

            next_move = path[1] 
            
            if self.graph.nodes[next_move].get('agent') == 'police':
                print(f"Caminho para o {port} esta bloqueado.")
                print(f"O ladrao encontrou um policial em {next_move} e precisa escolher outro caminho.")
                return False
        
            #usamos escolha gulosa onde o pi = igual a menor global dos caminhos
            if best_option is None or distances[port] < best_option[0]:
                best_option = (distances[port], path)

        if best_option:
            _, path = best_option
            next_move = path[1]

            if self.graph.nodes[self.position].get('agent') == 'thief':
                del self.graph.nodes[self.position]['agent']
            
            self.position = next_move
            self.graph.nodes[self.position]['agent'] = 'thief'

            print(f"O ladrao se moveu para {next_move}.")

            return True
            
        print("Todos os caminhos estão bloqueados. O ladrão perdeu")
        return False



        

        

