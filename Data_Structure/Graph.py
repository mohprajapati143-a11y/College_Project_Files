graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

print("Graph (Adjacency List):")
for node in graph:
    print(f"{node} -> {graph[node]}")


#B PART

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    print("\nBFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors to queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

bfs(graph, 0)




def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("\nDFS Traversal:", end=" ")
dfs(graph, 0)