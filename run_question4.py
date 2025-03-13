import time
from grid_graph import generate_weighted_grid_graph
from dijkstra_algos.dijkstra import *
from pq import APQUnsortedList


"""

Create 10 grid-graphs, each of size 500x500
    Every time a graph is created, do:
        for graph_instance, loop increasing end vertex distance
            call and time each:
                dijkstra_source_to_dest(graph, start, end,  apq_class, break_if_end_found=False)
                dijkstra_source_to_dest(graph, start, end,  apq_class, break_if_end_found=True)
"""

def benchmark_early_break_dijkstra(graph):
    pass

def benchmark_all_nodes_dijkstra(target, graph_set, if_found_break):

    total_time = 0
    for graph in graph_set:
        start_vertex = graph.get_vertex_by_label((250, 250))
        end_vertex = graph.get_vertex_by_label(target)
        start_time = time.perf_counter()
        # don't need to catch results as I'm only interested in the timing
        dijkstra_source_to_dest(graph, start_vertex, end_vertex, APQUnsortedList, if_found_break)
        total_time += time.perf_counter() - start_time

    avg_time = total_time / len(graph_set)

    return avg_time



if __name__ == "__main__":

    # Fixing the graph instances so we hae a consistent run
    graph_set = []
    # Going to create 10 grid-graphs and get the average dijkstra per target vertices
    for i in range(10):
        graph_set.append(generate_weighted_grid_graph(500, 500))

    # Choosing to go diagonal away from source vertex
    target_vertices = [(i, i) for i in range(251, 501)]

    print(" Target | All Node Timing | Early Break Timing")

    for target in target_vertices:

        # if_found_break controls breaking if target found or not
        early_break = benchmark_all_nodes_dijkstra(target, graph_set, if_found_break=True)
        no_early_break = benchmark_all_nodes_dijkstra(target, graph_set, if_found_break=False)
        print(f'{target} | {no_early_break} | {early_break}')
