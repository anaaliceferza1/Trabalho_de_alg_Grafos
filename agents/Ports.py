from graph.Create_graphos import Dgraphs
import networkx as nx

class Port:
    def __init__(self, graph = None):
        self.graph = graph
        self.ports = []

    def position(self):
        sorted_nodes = sorted(
            self.graph.graph.nodes(), 
            key=lambda n: self.graph.graph.nodes()[n]['altitude']
        ) 
        
        self.ports = sorted_nodes[:6]
        print(f"The ports are located at: {', '.join(self.ports)}.")

        for port in self.ports:
            self.graph.graph.nodes()[port]['agent'] = 'port'
        
        return self.ports
    
    def entry_degree(self):
        entry_edge = 0

        for edge in self.graph.graph.edges():
            if edge[1] in self.ports:
                entry_edge += self.graph.graph.edges[edge]['weight']
        
        print(f"The total entry degree of the ports is: {entry_edge}.")

        return entry_edge

