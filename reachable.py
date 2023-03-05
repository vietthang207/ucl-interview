from collections import deque

def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node
 
    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    num_vertices = len(adj_list)
    is_visited = []
    for i in range(num_vertices):
      is_visited.append(False)
    
    queue = deque(maxlen=num_vertices)
    queue.append(start_node)
    while len(queue) > 0:
      current = queue.popleft()
      if is_visited[current] == False:
        is_visited[current] = True
        for next in adj_list[current]:
          if is_visited[next] == False:
            queue.append(next)
    reached = set()
    for i in range(num_vertices):
      if is_visited[i]:
        reached.add(i)
    return reached
