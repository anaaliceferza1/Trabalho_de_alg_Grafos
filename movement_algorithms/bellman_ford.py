class Bellman_ford():
    def __init__(self, graph):
        self.graph = graph

    def alg_bellman_ford(self, start_node):
        '''
         O relaxamento ta funcionavel
        ........      
        '''
        cust = {}
        prev = {}

        for node in self.graph.nodes():
            cust[node] = float('inf')
            prev[node] = None

        cust[start_node] = 0

        for _ in range(len(self.graph.nodes()) - 1):
            updated = False
            for u, v, data in self.graph.edges(data=True):
                if 'weight' not in data:
                    continue

                w = data['weight']
                if cust[u] + w < cust[v]:
                    cust[v] = cust[u] + w
                    prev[v] = u
                    updated = True

            if not updated:
                break

        for u, v, data in self.graph.edges(data=True):
            if 'weight' not in data:
                continue

            if cust[u] + data['weight'] < cust[v]:
                return cust, prev, (u, v)

        return cust, prev, None

    def killing_negative_cycles(self):
        while True:
            _, _, cycle_edge = self.alg_bellman_ford(
                next(iter(self.graph.nodes()))
            )

            if not cycle_edge:
                break
            else:
                self.graph.remove_edge(*cycle_edge)

    def reconstruct_paths(self, prev, start_node, destination):
        path = []
        aux = destination

        while aux is not None:
            path.append(aux)
            aux = prev[aux]

        path.reverse()

        if not path or path[0] != start_node:
            return None

        return path
