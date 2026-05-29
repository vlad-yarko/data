import random

def linear_search_2d(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return (i, j)
    return (-1, -1)

matrix = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
target = matrix[5][7]

result = linear_search_2d(matrix, target)
print(f"Target {target} found at: {result}")

not_found = linear_search_2d(matrix, 999)
print(f"Target 999 found at: {not_found}")
