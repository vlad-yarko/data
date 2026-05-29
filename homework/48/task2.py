import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

data = random.sample(range(100000), 10000)
arr_copy = data[:]

start = time.time()
bubble_sort(data)
end = time.time()
print(f"Bubble Sort time: {end - start:.4f} c")

start = time.time()
arr_copy.sort()
end = time.time()
print(f"Built-in sort time: {end - start:.4f} c")
