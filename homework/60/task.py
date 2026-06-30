import json
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v, directed=False):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
        if not directed:
            self.graph[v].append(u)
            self.vertices.add(v)
    
    def is_connected(self):
        if not self.vertices:
            return True
        
        visited = set()
        start = next(iter(self.vertices))
        
        def dfs(v):
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(start)
        return len(visited) == len(self.vertices)
    
    def get_connected_components(self):
        visited = set()
        components = []
        
        def dfs(v, component):
            visited.add(v)
            component.append(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs(neighbor, component)
        
        for vertex in self.vertices:
            if vertex not in visited:
                component = []
                dfs(vertex, component)
                components.append(component)
        
        return components
    
    def has_cycle(self):
        visited = set()
        rec_stack = set()
        cycle_path = []
        
        def dfs(v, path):
            visited.add(v)
            rec_stack.add(v)
            path.append(v)
            
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    if dfs(neighbor, path.copy()):
                        return True
                elif neighbor in rec_stack:
                    cycle_path.extend(path + [neighbor])
                    return True
            
            rec_stack.remove(v)
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if dfs(vertex, []):
                    return True, cycle_path
        
        return False, []
    
    def tarjan_scc(self):
        index_counter = [0]
        stack = []
        lowlinks = {}
        index = {}
        on_stack = set()
        sccs = []
        
        def strongconnect(v):
            index[v] = index_counter[0]
            lowlinks[v] = index_counter[0]
            index_counter[0] += 1
            stack.append(v)
            on_stack.add(v)
            
            for w in self.graph[v]:
                if w not in index:
                    strongconnect(w)
                    lowlinks[v] = min(lowlinks[v], lowlinks[w])
                elif w in on_stack:
                    lowlinks[v] = min(lowlinks[v], index[w])
            
            if lowlinks[v] == index[v]:
                scc = []
                while True:
                    w = stack.pop()
                    on_stack.remove(w)
                    scc.append(w)
                    if w == v:
                        break
                sccs.append(scc)
        
        for v in self.vertices:
            if v not in index:
                strongconnect(v)
        
        return sccs
    
    def load_from_json(self, filename, directed=False):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for u, neighbors in data.items():
                    for v in neighbors:
                        self.add_edge(u, v, directed)
            return True
        except Exception as e:
            print(f"Error loading file: {e}")
            return False
    
    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(dict(self.graph), f)

def main():
    graph = Graph()
    directed = False
    loaded = False
    
    while True:
        print("\n=== Graph Analysis Tool ===")
        print("1. Load graph from JSON")
        print("2. Add edge manually")
        print("3. Check connectivity")
        print("4. Find connected components")
        print("5. Detect cycle")
        print("6. Find strongly connected components (Tarjan)")
        print("7. Exit")
        
        choice = input("Select operation (1-7): ").strip()
        
        if choice == '1':
            filename = input("Enter filename: ").strip()
            directed = input("Is graph directed? (y/n): ").strip().lower() == 'y'
            if graph.load_from_json(filename, directed):
                loaded = True
                print(f"Graph loaded. Vertices: {graph.vertices}")
        
        elif choice == '2':
            u = input("Enter source vertex: ").strip()
            v = input("Enter destination vertex: ").strip()
            graph.add_edge(u, v, directed)
            print(f"Edge {u} -> {v} added")
        
        elif choice == '3':
            if not graph.vertices:
                print("Graph is empty")
            elif graph.is_connected():
                print("Graph is CONNECTED")
            else:
                print("Graph is NOT CONNECTED")
                components = graph.get_connected_components()
                print(f"Connected components: {components}")
        
        elif choice == '4':
            if not graph.vertices:
                print("Graph is empty")
            else:
                components = graph.get_connected_components()
                print(f"Connected components ({len(components)}):")
                for i, comp in enumerate(components):
                    print(f"  Component {i + 1}: {comp}")
        
        elif choice == '5':
            if not graph.vertices:
                print("Graph is empty")
            else:
                has_cycle, cycle = graph.has_cycle()
                if has_cycle:
                    print("Cycle FOUND")
                    print(f"Cycle vertices: {set(cycle)}")
                else:
                    print("NO cycle found")
        
        elif choice == '6':
            if not graph.vertices:
                print("Graph is empty")
            else:
                sccs = graph.tarjan_scc()
                print(f"Strongly connected components ({len(sccs)}):")
                for i, scc in enumerate(sccs):
                    print(f"  SCC {i + 1}: {scc}")
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
