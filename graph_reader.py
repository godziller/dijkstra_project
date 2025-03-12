from pq.apq_unsorted_list import APQUnsortedList
from graph.graph_dijkstra import Graph
from dijkstra_algos.dijkstra import *


def graphreader(filename):
    """ Read and return the route map in filename. """
    graph = Graph()

    with open(filename, 'r') as file:  # Ensures the file is closed properly
        entry = file.readline().strip()  # Read first entry (Node or Edge)
        num_vertices = 0

        # Read Nodes
        while entry == 'Node':
            num_vertices += 1
            node_id = int(file.readline().split()[1])
            graph.add_vertex(node_id)
            entry = file.readline().strip()  # Read next line

        print(f"GraphReader - Read {num_vertices} vertices and added into the graph")

        num_edges = 0

        # Read Edges
        while entry == 'Edge':
            num_edges += 1
            source = int(file.readline().split()[1])
            target = int(file.readline().split()[1])
            length = float(file.readline().split()[1])

            sv = graph.get_vertex_by_label(source)
            tv = graph.get_vertex_by_label(target)
            graph.add_edge(sv, tv, length)

            file.readline()  # Read the one-way data
            entry = file.readline().strip()  # Read next entry (Node or Edge)

        print(f"GraphReader - Read {num_edges} edges and added into the graph")

    print(graph)
    return graph


def print_shortest_path(start, end, parent_map):
    """ Reconstruct and print the shortest path from start to end using the parent dictionary. """
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent_map[current]

    path.reverse()  # Reverse to get the correct order
    print(f"Path from {start} to {end}: {' -> '.join(str(v) for v in path)}")


if __name__ == "__main__":
    # Read Graph from File
    graph = graphreader("simplegraph2-2.txt")

    # Define Start and End Vertices
    start_vertex = graph.get_vertex_by_label(14)
    end_vertex = graph.get_vertex_by_label(5)

    # Run Dijkstra’s Algorithm
    #result = graph.dijkstra(start_vertex, end_vertex, PriorityQueue)
    results = dijkstra_source_to_dest(graph, start_vertex, end_vertex, APQUnsortedList)
    # Extract distances and parents from result
    distances = {v: results[v][0] for v in results}
    parents = {v: results[v][1] for v in results}

    # Print Distances
    print("\nShortest distances from start vertex:")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")

    # Print Shortest Paths
    print("\nShortest paths:")
    for vertex in distances:
        if vertex != start_vertex:
            print_shortest_path(start_vertex, vertex, parents)
