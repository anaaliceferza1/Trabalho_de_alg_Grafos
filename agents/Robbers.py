from graph.Create_graphos import Dgraphs
import networkx as nx   

class Robber:
    def __init__(self, graph = None):
        self.graph = graph
        self.castale = None
    
    def steal(self):
        print("O ladrao esta roubando!")

    def starting_position(self, graph):
        
        self.castale = max(self.graph.nodes(), key=lambda n: self.graph.nodes[n]['altitude']) #define o castelo como o vértice de maior altitude
       
        print(f"O ladrao esta no {castale}.")

        graph.graph.nodes()[castale]['agent'] = 'thief'
       
    #def move(self, graph, destination):      