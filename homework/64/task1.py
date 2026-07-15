class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        if self.table[index]:
            self.collisions += 1
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False
    
    def get_collisions(self):
        return self.collisions

import random
data = [(f"key_{i}", f"value_{i}") for i in range(1000)]
random.shuffle(data)

sizes = [10, 50, 100, 500, 1000]
print("Size\tCollisions\tCollision Rate")
for size in sizes:
    ht = MyHashTable(size)
    for key, value in data:
        ht.insert(key, value)
    collision_rate = (ht.get_collisions() / len(data)) * 100
    print(f"{size}\t{ht.get_collisions()}\t\t{collision_rate:.2f}%")
