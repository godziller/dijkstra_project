import random
from graph.graph_dijkstra import Graph

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


if __name__ == "__main__":
    n, m = 4, 5
    grid_graph = generate_weighted_grid_graph(n, m)
    print(grid_graph)
