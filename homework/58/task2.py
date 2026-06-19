import time
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs_shortest_path(self, start, end):
        visited = {start}
        queue = deque([(start, [start])])
        
        while queue:
            node, path = queue.popleft()
            if node == end:
                return path
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def dfs_shortest_path(self, start, end):
        visited = set()
        path = []
        shortest = [None]
        
        def dfs(node, target, current_path):
            if node == target:
                if shortest[0] is None or len(current_path) < len(shortest[0]):
                    shortest[0] = current_path[:]
                return
            
            if node in visited:
                return
            visited.add(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    current_path.append(neighbor)
                    dfs(neighbor, target, current_path)
                    current_path.pop()
            
            visited.discard(node)
        
        dfs(start, end, [start])
        return shortest[0]

graph1 = Graph()
for i in range(10):
    graph1.add_edge(i, (i + 1) % 10)
    graph1.add_edge(i, (i + 3) % 10)

start, end = 0, 5

t1 = time.time()
bfs_path = graph1.bfs_shortest_path(start, end)
t_bfs = time.time() - t1

t1 = time.time()
dfs_path = graph1.dfs_shortest_path(start, end)
t_dfs = time.time() - t1

print(f"10 vertices: BFS path: {bfs_path}, time: {t_bfs:.6f}s")
print(f"10 vertices: DFS path: {dfs_path}, time: {t_dfs:.6f}s")

graph2 = Graph()
for i in range(100):
    graph2.add_edge(i, (i + 1) % 100)
    graph2.add_edge(i, (i + 5) % 100)

start, end = 0, 50

t1 = time.time()
bfs_path = graph2.bfs_shortest_path(start, end)
t_bfs = time.time() - t1

t1 = time.time()
dfs_path = graph2.dfs_shortest_path(start, end)
t_dfs = time.time() - t1

print(f"100 vertices: BFS time: {t_bfs:.6f}s")
print(f"100 vertices: DFS time: {t_dfs:.6f}s")
