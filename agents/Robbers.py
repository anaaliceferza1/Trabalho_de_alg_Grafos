from graph.Create_graphos import Dgraphs
import networkx as nx   

class Robber:
    def __init__(self, graph = None):
        self.graph = graph
    
    def steal(self):
        print("O ladrao esta roubando!")

    def position(self, graph):
        castale = max(graph.graph.nodes(), key=lambda n: graph.graph.nodes()[n]['altitude']) #define o castelo como o vértice de maior altitude
       
        print(f"O ladrao esta no {castale}.")

        graph.graph.nodes()[castale]['agent'] = 'thief'
       
    #def move(self, graph, destination):      