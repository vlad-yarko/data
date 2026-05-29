import random

def linear_search_lambda(arr, condition):
    for i in range(len(arr)):
        if condition(arr[i]):
            return i
    return -1

data = [random.randint(1, 100) for _ in range(100)]

first_even = linear_search_lambda(data, lambda x: x % 2 == 0)
first_over_50 = linear_search_lambda(data, lambda x: x > 50)
first_divisible_by_3 = linear_search_lambda(data, lambda x: x % 3 == 0)

print(f"First even at index: {first_even} (value: {data[first_even] if first_even != -1 else 'N/A'})")
print(f"First > 50 at index: {first_over_50} (value: {data[first_over_50] if first_over_50 != -1 else 'N/A'})")
print(f"First divisible by 3 at index: {first_divisible_by_3} (value: {data[first_divisible_by_3] if first_divisible_by_3 != -1 else 'N/A'})")
