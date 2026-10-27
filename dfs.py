
def dfs(graph, curr_node, goal, visited, path):
    if curr_node == goal:
        return path.copy()

    visited[curr_node] = True

    for next_node in range(len(graph)):
        if graph[curr_node][next_node] == 1 and not visited[next_node]:
            path.append(next_node)

            result = dfs(graph, next_node, goal, visited, path)

            if result:
                return result

            path.pop()

    return None


print("==========================================")
print("       DFS Path Finding")
print("==========================================")

# Number of nodes
n = int(input("Enter number of nodes: "))

# Node names
nodes = input("Enter node names separated by spaces: ").split()

while len(nodes) != n or len(set(nodes)) != n:
    print(f"Enter exactly {n} unique node names.")
    nodes = input("Enter node names: ").split()

# Adjacency matrix
print("\nEnter the adjacency matrix:")
print("Enter 1 for connection and 0 for no connection.\n")

graph = []

for i in range(n):
    while True:
        row = list(map(int, input(
            f"Connections from {nodes[i]}: "
        ).split()))

        if len(row) == n:
            graph.append(row)
            break

        print(f"Please enter exactly {n} values.")

# Starting and goal nodes
start_name = input("\nEnter starting node: ")
goal_name = input("Enter goal node: ")

if start_name not in nodes or goal_name not in nodes:
    print("Invalid starting or goal node!")

else:
    start = nodes.index(start_name)
    goal = nodes.index(goal_name)

    visited = [False] * n
    path = [start]

    result = dfs(graph, start, goal, visited, path)

    print("\n==========================================")
    print("                 RESULT")
    print("==========================================")

    if result:
        print("Path found:", " -> ".join(nodes[i] for i in result))
        print("Path length:", len(result) - 1)
    else:
        print("No path exists.")
