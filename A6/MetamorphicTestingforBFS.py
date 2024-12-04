from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None


def test_mr_remove_edge():
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': []
    }
    path_before = bfs_shortest_path(graph, 'A', 'C')
    
    # Removing the edge between 'B' and 'C'
    graph['B'].remove('C')
    
    path_after = bfs_shortest_path(graph, 'A', 'C')
    
    assert path_after is None

if __name__ == "__main__":
    test_mr_remove_edge()
    print("Metamorphic test for removing edge passed.")
