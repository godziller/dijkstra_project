from pq import APQUnsortedList

def dijkstra_source_to_dest(graph, start, end,  apq_class, break_if_end_found=False):
    """
    Computes the shortest path from a given source vertex to a specified destination vertex
    using Dijkstra's algorithm with an Adaptable Priority Queue.

    Args:
        graph -- The Graph instance containing vertices and weighted edges.
        start -- The starting vertex for the shortest path calculation.
        end -- The destination vertex where the shortest path terminates.
        apq_class -- taking advantage that both APQ implemenations share same APIs
        break_if_end_found -- this allows the algo to exit early if the target is found

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
    pq = apq_class()

    # I needed this dict to track so I could use the APQ update_key later
    # without it, I would be limited to just adding - and duplicating entries :-(
    pq_elements = {}
    pq_elements[start] = pq.add(0, start)

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
        for neighbor in graph._structure[current]:

            # Get the edge reference to get the distance
            edge = graph._structure[current][neighbor]
            new_distance = distances[current] + edge.element()

            # Have I seen before? If so is this shorter? These will be infinity set earlier for first time observation.
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current

                # This is where the APQ update_key kicks in - distance represents priority
                # so if it is already in the apq, then update, otherwise just add.
                if neighbor in pq_elements:
                    pq.update_key(pq_elements[neighbor], new_distance)
                else:
                    pq_elements[neighbor] = pq.add(new_distance, neighbor)
    # return the closed dictionary.
    return closed
