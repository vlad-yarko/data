import time
import random

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

data = random.sample(range(1000), 100)

arr1 = data[:]
start = time.time()
insertion_sort(arr1)
t1 = time.time() - start
print(f"Insertion Sort: {t1:.6f} c")

arr2 = data[:]
start = time.time()
selection_sort(arr2)
t2 = time.time() - start
print(f"Selection Sort: {t2:.6f} c")

arr3 = data[:]
start = time.time()
arr3 = quick_sort(arr3)
t3 = time.time() - start
print(f"Quick Sort: {t3:.6f} c")
