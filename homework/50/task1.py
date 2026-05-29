def selection_sort_max(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        max_idx = 0
        for j in range(1, i + 1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[max_idx], arr[i] = arr[i], arr[max_idx]

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort_max(arr)
print(arr)
