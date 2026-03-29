import networkx as nx
import math

class Cops:
    def __init__(self, name = None, graph = None):
        self.graph = graph
        self.positions = []
        self.police_team = None
        self.name = name if name else "police"

    def arrest(self, suspect):
        print(f"{self.name} prendeu {suspect}.")

    def patrol(self):
        print(f"{self.name} estah patrulhando a area.")
    
    def cops_quantity(self, number):
        print(f"{self.name} has {number} estao patrulhando.")

    def number_of_cops(self, number, entrey_degree):
        cops_needes = number
        #agora so vai validar a quantidade de policiais com base no grau de entrada dos portos e na quantidade de nós do grafo
        n = len(self.graph.nodes())
        floor = math.isqrt(n)
        roof = entrey_degree

        if cops_needes <= floor:
            raise ValueError(f"Numero de equipe de policiais necessarios ({cops_needes}) nao pode ser menor ou igual a: {floor}.")
        elif cops_needes > roof:
            raise ValueError(f"Numero de equipe de policiais necessarios ({cops_needes}) nao pode ser maior que: {roof}.")
        else:
            print(f"Numero de equipe de policiais necessarios: {cops_needes}.")
        
    #pra salvar oque foi passado no 
    def set_positions(self, positions):
        self.positions = positions

        for p in positions:
            self.graph.nodes[p]['agent'] = 'police'
    
    def police_vehicle():

        print("viatura criada")
        

        