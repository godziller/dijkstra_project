from run_question4 import *
from pq import *



if __name__ == "__main__":

    # Fixing the graph instances so we hae a consistent run
    graph_set = []
    # Going to create 10 grid-graphs and get the average dijkstra per target vertices
    for i in range(1):
        graph_set.append(generate_weighted_grid_graph(500, 500))

    # Choosing to go diagonal away from source vertex
    target_vertices = [(i, i) for i in range(251, 501)]

    print(" Target | All Node Timing - Unsorted | Early Break Timing - Unsorted | "
          "All Node Timing - PQ | Early Break Timing - PQ")

    for target in target_vertices:
        # if_found_break controls breaking if target found or not
        early_break_unsorted_apq = benchmark_all_nodes_dijkstra(target, APQUnsortedList, graph_set, if_found_break=True)
        no_early_break_unsorted_apq = benchmark_all_nodes_dijkstra(target, APQUnsortedList, graph_set, if_found_break=False)
        early_break_vanilla_pq = benchmark_all_nodes_dijkstra(target, PriorityQueue, graph_set, if_found_break=True)
        no_early_break_vanilla_pq = benchmark_all_nodes_dijkstra(target, PriorityQueue, graph_set, if_found_break=False)

        print(f'{target} | {no_early_break_unsorted_apq} | {early_break_unsorted_apq}| '
              f'{no_early_break_vanilla_pq} | {early_break_vanilla_pq}')