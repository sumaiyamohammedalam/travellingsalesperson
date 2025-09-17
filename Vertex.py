class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())

    # New method: get weight of edge to a specific vertex
    def get_edge_weight(self, vertex):
        return self.edges.get(vertex, None)
