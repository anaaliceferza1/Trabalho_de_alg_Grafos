from graph.Create_graphos import Dgraphs
import networkx as nx

class Port:
    def __init__(self, graph = None):
        self.graph = graph
        self.ports = []

    def position(self, ports_nodes ):
        self.ports = ports_nodes
        
        print(f"Os portos estão localizados em: {', '.join(self.ports)}.")

        for port in self.ports:
            self.graph.nodes[port]['agent'] = 'port'
        
        return self.ports
    
    def entry_degree(self):
        entry_edge = 0

        for u, v, data in self.graph.edges(data=True):
            if v in self.ports:
                entry_edge += data['weight']
        
        print(f"O grau de entrada dos portos é: {entry_edge}.")

        return entry_edge

