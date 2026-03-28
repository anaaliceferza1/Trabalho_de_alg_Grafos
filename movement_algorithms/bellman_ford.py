
from graph.Create_graphos import Dgraphs

class Bellman_ford():
    def __init__(self, graph):
        self.graph =  graph

    def alg_bellman_ford(self, start_node):
        dist = {v: float('inf') for v in self.graph.nodes()}
        prev = {v: None for v in self.graph.nodes()}

        dist[start_node] = 0

        for _ in range(len(self.graph.nodes())-1):
            updated = False
            for u,v,data in self.graph.edges(data=True):
                if 'weight' not in data: 
                    continue

                w = data['weight']

                if (dist[u] + w) < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
            if not updated:
                break
            
        for u, v, data in self.graph.edges(data=True):
            if 'weight' not in data:
                continue
            if dist[u] + data['weight'] < dist[v]:
                return dist, prev, (u, v)
            
        return dist, prev, None

    def killing_negative_cycles(self):
            while True:
                _, _,cycle_edge =  self.alg_bellman_ford(next(iter(self.graph.nodes())))
                if not cycle_edge:
                    break
                else:
                    self.graph.remove_edge(*cycle_edge)


    def reconstruct_paths(self, prev, start_node, destination):
        path = []
        aux =  destination

        while aux is not None:
            path.append(aux)
            aux = prev[aux]

        path = list(reversed(path))

        if not path or path[0] != start_node:
            return None
        return path