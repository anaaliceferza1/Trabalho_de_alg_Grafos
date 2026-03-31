
import networkx as nx

class Port:
    def __init__(self, graph = None):
        self.graph = graph
        self.ports = []

    def set_position(self, ports_nodes):
        self.ports = ports_nodes
        
        print(f"\n\status: \n1. Os portos estão localizados em: {', '.join(self.ports)}.")

        for port in self.ports:
            self.graph.nodes[port]['agent'] = 'port'
    
    #calculo de entrada dos portos corrigida apos teste
    #testando sem peso 
    def entry_degree(self):
        entry_edge = 0

        #modificaçao da contagem ja que o grafo nao e mais direcionado
        for v in self.ports:
            for _ in self.graph.neighbors(v):
                entry_edge += 1
        
        print(f"2 .O grau de entrada dos portos é: {entry_edge}.")

        return entry_edge

