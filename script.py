import random
from Graph import Graph
from Vertex import Vertex

# Utility: print the graph
def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex + " (weight: " + str(vertex_neighbors[adjacent_vertex]) + ")")

# Build a sample TSP graph
def build_tsp_graph(directed=False):
    g = Graph(directed)
    vertices = []
    for val in ['a', 'b', 'c', 'd']:
        vertex = Vertex(val)
        vertices.append(vertex)
        g.add_vertex(vertex)

    g.add_edge(vertices[0], vertices[1], 3)
    g.add_edge(vertices[0], vertices[2], 4)
    g.add_edge(vertices[0], vertices[3], 5)
    g.add_edge(vertices[1], vertices[0], 3)
    g.add_edge(vertices[1], vertices[2], 2)
    g.add_edge(vertices[1], vertices[3], 6)
    g.add_edge(vertices[2], vertices[0], 4)
    g.add_edge(vertices[2], vertices[1], 2)
    g.add_edge(vertices[2], vertices[3], 1)
    g.add_edge(vertices[3], vertices[0], 5)
    g.add_edge(vertices[3], vertices[1], 6)
    g.add_edge(vertices[3], vertices[2], 1)
    return g

# Helper: check if all vertices are visited
def all_visited(visited_vertices):
    return all(status == "visited" for status in visited_vertices.values())

# Traveling Salesperson (greedy approach)
def traveling_salesperson(graph):
    final_path = ""
    visited_vertices = {vertex: "unvisited" for vertex in graph.graph_dict}

    # Pick a random starting vertex
    current_vertex = random.choice(list(graph.graph_dict.keys()))
    visited_vertices[current_vertex] = "visited"
    final_path += current_vertex

    visited_all_vertices = all_visited(visited_vertices)

    while not visited_all_vertices:
        # Copy edges to avoid modifying original graph
        edges_dict = graph.graph_dict[current_vertex].edges.copy()

        found_next_vertex = False
        next_vertex = ""

        while not found_next_vertex:
            if not edges_dict:
                break  # No edges left
            # Pick neighbor with minimum weight
            next_vertex_candidate = min(edges_dict, key=edges_dict.get)
            if visited_vertices[next_vertex_candidate] == "unvisited":
                next_vertex = next_vertex_candidate
                found_next_vertex = True
            else:
                edges_dict.pop(next_vertex_candidate)

        if not found_next_vertex:
            visited_all_vertices = True
        else:
            current_vertex = next_vertex
            visited_vertices[current_vertex] = "visited"
            final_path += " -> " + current_vertex

        visited_all_vertices = all_visited(visited_vertices)

    # Optional: return to starting vertex to complete cycle
    start_vertex = final_path.split(" -> ")[0]
    final_path += " -> " + start_vertex

    print("TSP path:", final_path)

# Main execution
if __name__ == "__main__":
    tsp_graph = build_tsp_graph(directed=False)
    print_graph(tsp_graph)
    traveling_salesperson(tsp_graph)
