import time
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

data = [random.randint(1, 100000) for _ in range(10000)]

target_start = data[0]
target_middle = data[5000]
target_end = data[9999]

start = time.time()
linear_search(data, target_start)
t_start = time.time() - start

start = time.time()
linear_search(data, target_middle)
t_middle = time.time() - start

start = time.time()
linear_search(data, target_end)
t_end = time.time() - start

print(f"Start: {t_start:.6f} c")
print(f"Middle: {t_middle:.6f} c")
print(f"End: {t_end:.6f} c")
