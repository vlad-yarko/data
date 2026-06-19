from collections import deque, defaultdict

class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_connection(self, person1, person2):
        self.graph[person1].append(person2)
        self.graph[person2].append(person1)
    
    def bfs_within_distance(self, start, max_distance):
        visited = {start}
        queue = deque([(start, 0)])
        result = []
        
        while queue:
            person, distance = queue.popleft()
            if distance <= max_distance:
                if person != start:
                    result.append((person, distance))
            
            if distance < max_distance:
                for neighbor in self.graph[person]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
        
        return result

network = SocialNetwork()
network.add_connection("Alice", "Bob")
network.add_connection("Alice", "Charlie")
network.add_connection("Bob", "Diana")
network.add_connection("Charlie", "Eve")
network.add_connection("Diana", "Frank")

result = network.bfs_within_distance("Alice", 2)
print("People within 2 steps from Alice:")
for person, distance in sorted(set((p, d) for p, d in result)):
    print(f"  {person} (distance: {distance})")
