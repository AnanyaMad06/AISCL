
from queue import PriorityQueue


def best_first_search(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    visited = set()
    parent = {start: None}

    while not pq.empty():
        h, current = pq.get()

        if current in visited:
            continue

        print("Visited:", current)
        visited.add(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = current

                pq.put((heuristic[neighbor], neighbor))

    if goal not in visited:
        print("\nNo path found!")
        return

    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nPath Found:", " -> ".join(path))


print("==========================================")
print("    Greedy Best-First Search")
print("==========================================")

# Number of nodes
n = int(input("Enter number of nodes: "))

graph = {}
heuristic = {}

# Enter node names and heuristic values
print("\nEnter node details:")

while len(graph) < n:
    node = input("\nNode name: ")

    if node in graph:
        print("Node already exists! Enter a unique name.")
        continue

    h = int(input(f"Heuristic value of {node}: "))
    heuristic[node] = h
    graph[node] = []

# Enter connections
print("\nEnter connections for each node:")

for node in graph:
    neighbors = input(
        f"Enter neighbors of {node} (space separated): "
    ).split()

    while any(neighbor not in graph for neighbor in neighbors):
        print("Invalid neighbor! Enter only defined node names.")
        neighbors = input(
            f"Enter neighbors of {node}: "
        ).split()

    graph[node] = neighbors

# Starting and goal nodes
start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")

if start not in graph or goal not in graph:
    print("Invalid starting or goal node!")
else:
    print("\nGreedy Best-First Search Traversal:")
    best_first_search(graph, heuristic, start, goal)
