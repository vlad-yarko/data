def min_ticket_cost(n):
    costs = [0] * (n + 1)
    
    for i in range(1, n + 1):
        cost1 = costs[i - 1] + 2
        cost3 = costs[max(0, i - 3)] + 5
        cost7 = costs[max(0, i - 7)] + 10
        costs[i] = min(cost1, cost3, cost7)
    
    return costs[n]

n = int(input("Enter number of days: "))
result = min_ticket_cost(n)
print(f"Minimum cost for {n} days: {result} grn")

for i in [1, 3, 4, 5, 7, 10, 15, 20]:
    print(f"Days {i}: {min_ticket_cost(i)} grn")
