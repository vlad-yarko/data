def insertion_sort_stable_check(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

test_data = [(3, 0), (1, 1), (3, 2), (2, 3)]
result = insertion_sort_stable_check(test_data)
print(result)

is_stable = all(result[i][1] < result[i + 1][1] for i in range(len(result) - 1) if result[i][0] == result[i + 1][0])
print(f"Insertion Sort is stable: {is_stable}")
