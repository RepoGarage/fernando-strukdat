# Graph - Structure Data

_Fernando Perry (233406005)_

## Code

```python
import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.con = []

    def add(self, node, cost):
        self.con.append([node, cost])

    def remove_connection(self, node):
        self.con = [c for c in self.con if c[0] != node]


def dijkstra(start, end):
    distances = {}
    previous = {}
    queue = []

    distances[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        for neighbor, cost in current_node.con:
            new_dist = current_dist + cost
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_dist, neighbor))

    path = []
    node = end
    while node != start:
        path.append(node)
        node = previous.get(node)
        if node is None:
            return None, float('inf')
    path.append(start)
    path.reverse()
    return path, distances[end]


if __name__ == "__main__":
    nodes = {}

    def find_node(name):
        return nodes.get(name)

    while True:
        print("1. Solve shortest path")
        print("2. Add node")
        print("3. Connect nodes")
        print("4. Delete node")
        print("5. List nodes")
        print("6. Exit")

        try:
            choice = int(input("Select option: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            src = input("  Start node: ")
            dst = input("  End node: ")
            start = find_node(src)
            end = find_node(dst)
            if start and end:
                path, dist = dijkstra(start, end)
                if path:
                    print(" -> ".join([node.name for node in path]), f"(Cost: {dist})")
                else:
                    print("No path found.")
            else:
                print("Invalid node name(s).")

        elif choice == 2:
            name = input("  Node name: ")
            if name in nodes:
                print("Node already exists.")
            else:
                nodes[name] = Node(name)
                print(f"Node '{name}' added.")

        elif choice == 3:
            src = input("  From node: ")
            dst = input("  To node: ")
            try:
                cost = int(input("  Cost: "))
            except ValueError:
                print("Cost must be an integer.")
                continue
            a = find_node(src)
            b = find_node(dst)
            if a and b:
                a.add(b, cost)
                print(f"Connected '{src}' to '{dst}' with cost {cost}")
            else:
                print("One or both nodes not found.")

        elif choice == 4:
            name = input("  Node name to delete: ")
            target = nodes.pop(name, None)
            if target:
                for node in nodes.values():
                    node.remove_connection(target)
                print(f"Node '{name}' deleted.")
            else:
                print("Node not found.")

        elif choice == 5:
            if not nodes:
                print("No nodes available.")
            else:
                for name, node in nodes.items():
                    connections = ", ".join([f"{n.name}({c})" for n, c in node.con])
                    print(f"{name}: {connections if connections else 'No connections'}")

        elif choice == 6:
            break

        else:
            print("Invalid option.")
```

## Run
```
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 2
  Node name: A
Node 'A' added.
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 2
  Node name: B
Node 'B' added.
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 3
  From node: A
  To node: B
  Cost: 2
Connected 'A' to 'B' with cost 2
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 5
A: B(2)
B: No connections
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 2
  Node name: C
Node 'C' added.
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 2
  Node name: D
Node 'D' added.
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 3
  From node: A
  To node: C
  Cost: 6
Connected 'A' to 'C' with cost 6
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 5
A: B(2), C(6)
B: No connections
C: No connections
D: No connections
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 3
  From node: B
  To node: D
  Cost: 1
Connected 'B' to 'D' with cost 1
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 3
  From node: B
  To node: C
  Cost: 10
Connected 'B' to 'C' with cost 10
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 5
A: B(2), C(6)
B: D(1), C(10)
C: No connections
D: No connections
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 3
  From node: C
  To node: D
  Cost: 3 
Connected 'C' to 'D' with cost 3
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 5
A: B(2), C(6)
B: D(1), C(10)
C: D(3)
D: No connections
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 1
  Start node: A
  End node: D
A -> B -> D (Cost: 3)
1. Solve shortest path
2. Add node
3. Connect nodes
4. Delete node
5. List nodes
6. Exit
Select option: 
```
