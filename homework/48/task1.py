def bubble_sort_stable_check(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

test_data = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]
bubble_sort_stable_check(test_data)
print(test_data)
