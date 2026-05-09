from collections import deque

queue = deque()

for name in ["Alice", "Bob", "Charlie"]:
    queue.append(name)

print("First in line:", queue[0])

while queue:
    print("Serving:", queue.popleft())
