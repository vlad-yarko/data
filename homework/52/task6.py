import random

def binary_search_recursive(arr, target, left, right, log):
    log.append(f"left={left}, right={right}")
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, log)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, log)

data = sorted([random.randint(1, 1000) for _ in range(100)])
target = data[50]

log = []
result = binary_search_recursive(data, target, 0, len(data) - 1, log)

print(f"Target {target} found at index: {result}")
print(f"Total calls: {len(log)}")
print(f"Call log:")
for i, call in enumerate(log):
    print(f"  {i + 1}: {call}")
