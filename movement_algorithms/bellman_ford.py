def bellman_ford(self, source):
        dist = {v: float('inf') for v in self.graph.nodes()}
        prev = {v: None for v in self.graph.nodes()}

        dist[source] = 0

        for _ in range(len(self.graph.nodes())-1):
            updated = False
            for u,v,data in self.graph.edges(data=True):
                if 'weight' not in data: 
                    print("Aresta sem peso", u, v)

                w = data['weight']
                if (dist[u] + w) < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
            if not updated:
                break
        for u,v,data in self.graph.edges(data=True):
            w = data['weight']
            if dist[u] + w < dist[v]:
                return dist,prev,(u,v)
        
        return dist, prev, None