import random
from graph import Graph
from dijkstra_algos.dijkstra import *
from pq import APQUnsortedList


def generate_weighted_grid_graph(n, m):
    """
    Generates a weighted grid graph of size n x m.

    Parameters:
    n (int): Number of rows in the grid.
    m (int): Number of columns in the grid.

    Returns:
    Graph: An instance of a grid-graph representing the weighted grid.

    Description:
    The function constructs a grid graph. NOTE: vertexs have neighbours to
    the south and east - 2 max. And only have a 1 predecessor point to it -
    this predecessor is either located to the north or west
    """

    graph = Graph()
    max_weight = max(n, m) // 2

    vertices = {}
    for i in range(n):
        for j in range(m):
            # Going to use the (i,j) as a tuple to identify each vertex
            vertices[(i, j)] = graph.add_vertex((i, j))

    for i in range(n):
        for j in range(m):
            if i + 1 < n:
                weight = random.randint(1, max_weight)
                graph.add_edge(vertices[(i, j)], vertices[(i + 1, j)], weight)
            if j + 1 < m:
                weight = random.randint(1, max_weight)
                graph.add_edge(vertices[(i, j)], vertices[(i, j + 1)], weight)

    return graph

def get_shortest_path(start, end, predecessors):
    """ Reconstruct and print the shortest path from start to end using the predecessors dictionary. """
    path = []
    # Working from end back to start, setting a tmp variable current to the end vertex
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]

    path.reverse()  # Reverse to make it more intuitive for printing
    return f"Path from {start} to {end}: {' -> '.join(str(v) for v in path)}"

if __name__ == "__main__":
    n, m = 4, 4
    grid_graph = generate_weighted_grid_graph(n, m)
    print(grid_graph)
    print("===================")
    # Using the i,j tuple as the vertex identifier now
    start_vertex = grid_graph.get_vertex_by_label((0,0))
    # and need to cater for indexing starting at 0 - ergo south east corner is -1
    end_vertex = grid_graph.get_vertex_by_label((n-1,m-1))

    # Run Dijkstra’s Algorithm with my unsorted APQ
    # also passing in instance to my graph
    results = dijkstra_source_to_dest(start_vertex, end_vertex, grid_graph, APQUnsortedList)

    # Extract distances and predecessor from result
    distances = {v: results[v][0] for v in results}
    predecessors = {v: results[v][1] for v in results}

    print("----------------")

    # Print Distances
    print("\nShortest distances from start vertex:")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")

    # Print Shortest Paths
    print("\nShortest paths:")
    for vertex in distances:
        if vertex != start_vertex:
            print(get_shortest_path(start_vertex, vertex, predecessors))

    # Now this is where I test if I work.... 14->5 = length 8 and predecessor 8
    print(f"Specific output from north west, {start_vertex} to {end_vertex}")
    target_distance = distances.get(end_vertex, 'Not reachable')
    print(f"\n\nDistance to {end_vertex} is {target_distance}")
    print(f"And {end_vertex}'s predecessor is {predecessors[end_vertex]}")
