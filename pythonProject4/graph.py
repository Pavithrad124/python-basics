from collections import deque

graph = {
    1: [2, 4],
    2: [3],
    3: [4],
    4: [1]
}

def traverse_graph(graph):
    for node, neighbors in graph.items():
        print(f"{node} -> {', '.join(map(str, neighbors))}")

traverse_graph(graph)

# DFS using an explicit stack (iterative approach)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Process the current node
            visited.add(node)
            # Add neighbors to the stack (reversed for correct order)
            stack.extend(reversed(graph[node]))
            # print(stack, end=" ")

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        print(node, end=" ")

        # Add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("\nDFS Iterative:")
dfs_iterative(graph, 1)

# Perform BFS
print("\nBFS Traversal:")
bfs(graph, 1)