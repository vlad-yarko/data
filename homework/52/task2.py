import time
import random
import sys

sys.setrecursionlimit(20000)

def linear_search_iterative(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def linear_search_recursive(arr, target, idx=0):
    if idx == len(arr):
        return -1
    if arr[idx] == target:
        return idx
    return linear_search_recursive(arr, target, idx + 1)

data = [random.randint(1, 100000) for _ in range(10000)]
target = data[5000]

start = time.time()
linear_search_iterative(data, target)
t_iterative = time.time() - start

start = time.time()
linear_search_recursive(data, target)
t_recursive = time.time() - start

print(f"Iterative: {t_iterative:.6f} c")
print(f"Recursive: {t_recursive:.6f} c")
print(f"Recursive uses more stack memory due to call depth")
