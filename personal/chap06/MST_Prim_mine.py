class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

def mst_prim(G, w, r):
    key = {node:float('inf') for node in G.vertices}
    predecessor = {node:None for node in G.vertices}
    
    pass