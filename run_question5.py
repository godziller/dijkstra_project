import time
from graph import Graph
from pq import APQBinaryHeap
from dijkstra_algos.dijkstra import *
from grid_graph import generate_weighted_grid_graph

# TOOO: Reusing the print functinon - should really move this into a util.py location
from run_question1 import print_shortest_path
from run_question2 import get_shortest_path

''' Similar to Q2, however, the end_vertex is not the south-east corner (n,m), 
    Rather the centre of the graph - n//2, m//2

    Going to have graphs from size 10 -> 500 in increments of 20 grid size so it will be:

    increment graph size by 20
        create & run 10 instances of this same grid size
            generate grid
            run dijkstra
            result = dijkstra average run - i.e. AVERGE of each 10 results of distra 
            print output something like: Graph size | PQ Used | time for dijkstra run 

'''


def benchmark_dijkstra_all_pqs():
    '''
    Runs Dijkstra's algorithm on grid graphs of increasing size, recording execution time.

    Parameters:
    - None
    Description:
    - Generates grid graphs from size 10x10 up to 500x500 in increments of 20.
    - For each grid size, runs 10 instances to compute an average runtime.
    - The destination vertex is the center of the graph (n//2, m//2) instead of the bottom-right corner.
    - Outputs the average execution time for each grid size.

    Output Format:
    Graph Size | PQ Used | Average Time (s)
    '''
    # Print the header before the loop
    print(f"{'Grid Size':<10} {'Binary Heap Time':<20} {'Unsorted List Time':<20}")

    for size in range(20, 501, 20):
        total_time_apq_binary_heap = 0
        total_time_apq_apq_unsorted_list = 0
        grid_size = size * size

        for _ in range(10):
            graph = generate_weighted_grid_graph(size, size)
            start_vertex = graph.get_vertex_by_label((0, 0))
            end_vertex = graph.get_vertex_by_label((size // 2, size // 2))

            start_time_apq_binary_heap = time.perf_counter()
            results_apq_binary_heap = dijkstra_source_to_dest(start_vertex, end_vertex, graph, APQBinaryHeap)
            total_time_apq_binary_heap += time.perf_counter() - start_time_apq_binary_heap

            start_time_apq_unsorted_list = time.perf_counter()
            results_apq_unsorted_list = dijkstra_source_to_dest(start_vertex, end_vertex, graph, APQUnsortedList)
            total_time_apq_apq_unsorted_list += time.perf_counter() - start_time_apq_unsorted_list

        avg_time_apq_unsorted_list = total_time_apq_apq_unsorted_list / 10
        avg_time_apq_binary_heap = total_time_apq_binary_heap / 10

        # Assuming the final path length asked for mean the last 2 vertexs from the run above.
        distances_binary_heap = {v: results_apq_binary_heap[v][0] for v in results_apq_binary_heap}
        final_path_length_binary_heap = distances_binary_heap.get(end_vertex, 'Not reachable')

        distances_unsorted_list = {v: results_apq_binary_heap[v][0] for v in results_apq_binary_heap}
        final_path_length_unsorted_list = distances_binary_heap.get(end_vertex, 'Not reachable')

        # Inside your loop:
        print(f"{grid_size:<10} {avg_time_apq_binary_heap:<20.6f} {avg_time_apq_unsorted_list:<20.6f}")

if __name__ == "__main__":
    benchmark_dijkstra_all_pqs()

