import time
import random

def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

data = sorted([random.randint(1, 1000000) for _ in range(100000)])
target = data[50000]

start = time.time()
lin_idx, lin_cmp = linear_search(data, target)
t_linear = time.time() - start

start = time.time()
bin_idx, bin_cmp = binary_search(data, target)
t_binary = time.time() - start

print(f"Linear Search: {t_linear:.6f} c, {lin_cmp} comparisons")
print(f"Binary Search: {t_binary:.6f} c, {bin_cmp} comparisons")
