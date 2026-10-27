
import heapq


def a_star(graph, heuristic, start, goal):
    # Priority queue: (f, g, current_node)
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start))

    # Cost of reaching each node
    g_cost = {start: 0}

    # Parent dictionary for path reconstruction
    parent = {start: None}

    while pq:
        f, g, current = heapq.heappop(pq)

        # Skip outdated entries
        if g > g_cost[current]:
            continue

        print("Visited:", current)

        # Goal reached
        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            return path, g_cost[goal]

        # Explore neighboring nodes
        for neighbor, cost in graph[current]:
            new_g = g + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current

                h = heuristic[neighbor]
                new_f = new_g + h

                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )

    return None, float("inf")


print("==========================================")
print("          A* GRAPH SEARCH")
print("==========================================")

# Number of nodes
n = int(input("Enter number of nodes: "))

graph = {}
heuristic = {}

# Enter node names and heuristic values
print("\nEnter node details:")

while len(graph) < n:
    node = input("Node name: ")

    if node in graph:
        print("Node already exists!")
        continue

    h = int(input(f"Heuristic value of {node}: "))

    graph[node] = []
    heuristic[node] = h

# Enter weighted, undirected connections
m = int(input("\nEnter number of edges: "))

print("Enter each edge as: node1 node2 cost")

for i in range(m):
    while True:
        u, v, cost = input(
            f"Edge {i + 1}: "
        ).split()

        cost = int(cost)

        if u not in graph or v not in graph:
            print("Invalid node name! Try again.")
            continue

        if cost < 0:
            print("Edge cost cannot be negative!")
            continue

        graph[u].append((v, cost))
        graph[v].append((u, cost))
        break

# Starting and goal nodes
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

if start not in graph or goal not in graph:
    print("Invalid start or goal node!")

else:
    print("\nA* Search Traversal:")

    path, total_cost = a_star(
        graph, heuristic, start, goal
    )

    print("\n==========================================")
    print("                 RESULT")
    print("==========================================")

    if path is None:
        print("No path found!")
    else:
        print("Path Found:", " -> ".join(path))
        print("Total Path Cost:", total_cost)
