from pq import APQUnsortedList

def dijkstra_source_to_dest(start, end, graph, pq_class, break_if_end_found=False):
    """
    Computes the shortest path from a given source vertex to a specified destination vertex
    using Dijkstra's algorithm with an Adaptable Priority Queue.

    Args:

        start -- The starting vertex for the shortest path calculation.
        end -- The destination vertex where the shortest path terminates.
        graph -- The Graph instance containing vertices and weighted edges.
        apq_class -- supporting APQ and standard PQ - APQUnsortedList, APQBinaryHeap, PriorityQueue
        break_if_end_found -- boolean controlling if the algo breaks out when finding target immediately or not.


    Returns:
        A closed dictionary containing
        - Vertex as the key.
        - value is a pair consisting of path length from source and preceding vertex.

    """

    # This dictionary stores the shortest known distance from the start vertex to each vertex, initialized to infinity.
    distances = {v: float('inf') for v in graph._structure}
    distances[start] = 0 # and overwriting infinity 'cos its zero weight to ourself.

    # This dictionary tracks the previous vertex for each vertex, allowing for path reconstruction.
    # with grid graph, each vertex has 2 neighbours, but only 1 vertex pointing to it. We don't know for each
    #   what this is yet - so setting everyone to None.
    predecessors = {v: None for v in graph._structure}

    # This comes in handy as our 2 APQ implemenations use the same apis, so we can save a bit of code here.
    # the caller of this function will specify which to use.
    pq = pq_class()

    # Ok, this is where I modify to cater for standard PriorityQueue class
    # The big difference here is such does not support the update_key feature of APQs.
    # Hence the flow of the below needs to cater for this.

    # We begin by creating a flag to control the flow - PQ vs APQ

    is_pq_adaptable = pq.__class__.__name__ != "PriorityQueue"

    # I needed this dict to track so I could use the APQ update_key later
    # without it, I would be limited to just adding - and duplicating entries :-(
    # For PQ - this is not needed/used - we end up adding dups.
    pq_elements = {}

    # Here is the first difference between 2 types
    if is_pq_adaptable:
        pq_elements[start] = pq.add(0, start)
    else:
        # I don't need to track - 'cos I'm adding dups.
        pq.add(0, start)

    # CLosed Dictionary where vertex is key, and value is a pair (length, preceding vertex)
    closed = {}

    while pq.length() > 0:
        current = pq.remove_min()

        # Move along, nothing to see  - already processed this vertex.
        if current in closed:
            continue

        # Ok, new vertex observed, record length and predecessor
        closed[current] = (distances[current], predecessors[current])

        # You have arrived, disembark the dijkstra train
        # This break_if_end_found allows us to exit quicker..
        if break_if_end_found and current == end:
            break

        # Look for neighbours for this current vertex - which will be east and south as we are a grid-graph
        # i.e. this loops twice - except for boundary vertexs
        for neighbour in graph._structure[current]:

            # Get the edge reference to get the distance
            edge = graph._structure[current][neighbour]
            new_distance = distances[current] + edge.element()

            # Have I seen before? If so is this shorter? These will be infinity set earlier for first time observation.
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                predecessors[neighbour] = current

                # This block is where the difference between queue types is seen in action
                # APQ take advantage of update_key
                # PQ has no such feature
                if is_pq_adaptable:
                    # This is where the APQ update_key kicks in - distance represents priority
                    # so if it is already in the apq, then update, otherwise just add.
                    if neighbour in pq_elements:
                        pq.update_key(pq_elements[neighbour], new_distance)
                    else:
                        pq_elements[neighbour] = pq.add(new_distance, neighbour)
                else:
                    pq.add(new_distance, neighbour)
    # return the closed dictionary.
    return closed


