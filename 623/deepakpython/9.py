from collections import deque

graph = {
    12: [10, 3, 7],
    10: [12, 7],
    7: [12, 10, 6],
    3: [12, 6],
    6: [7, 3]
}

def shortest_distance(graph, start, end):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))
    return -1

start_node = 12
end_node = 6

distance = shortest_distance(graph, start_node, end_node)
print(f"Shortest distance between {start_node} and {end_node} is:", distance)
