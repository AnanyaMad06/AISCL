
from collections import deque

def bfs(graph, start, goal):
    n = len(graph)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        for next_node in range(n):
            if graph[node][next_node] == 1 and next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, path + [next_node]))

    return None


print("===== BFS Path Finding =====")

n = int(input("Enter number of nodes: "))
nodes = input("Enter node names separated by spaces: ").split()

while len(nodes) != n:
    print(f"Please enter exactly {n} node names.")
    nodes = input("Enter node names: ").split()

print("\nEnter adjacency matrix (1 = connection, 0 = no connection):")

graph = []

for i in range(n):
    row = list(map(int, input(
        f"Connections from {nodes[i]}: "
    ).split()))

    while len(row) != n:
        print(f"Please enter exactly {n} values.")
        row = list(map(int, input(
            f"Connections from {nodes[i]}: "
        ).split()))

    graph.append(row)

start_name = input("Enter starting node: ")
goal_name = input("Enter goal node: ")

if start_name not in nodes or goal_name not in nodes:
    print("Invalid starting or goal node!")
else:
    start = nodes.index(start_name)
    goal = nodes.index(goal_name)

    path = bfs(graph, start, goal)

    print("\n========== RESULT ==========")

    if path:
        print("Path found:", " -> ".join(nodes[i] for i in path))
        print("Path length:", len(path) - 1)
    else:
        print("No path exists.")
