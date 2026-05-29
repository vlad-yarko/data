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
for val, pos in result:
    print(f"value={val}, original_pos={pos}")
