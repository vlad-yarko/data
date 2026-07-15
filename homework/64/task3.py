def multiplicative_hash(key, m, A):
    h = hash(key)
    return int(m * ((A * h) % 1))

def analyze_parameters(keys, m_values, A_values):
    results = {}
    
    for m in m_values:
        for A in A_values:
            hashes = [multiplicative_hash(k, m, A) for k in keys]
            
            distribution = [0] * m
            for h in hashes:
                distribution[h] += 1
            
            variance = sum((x - len(keys) / m) ** 2 for x in distribution) / m
            collisions = len(keys) - len(set(hashes))
            uniformity = 1 - (variance / (len(keys) ** 2 / m))
            
            results[(m, A)] = {
                'variance': variance,
                'collisions': collisions,
                'uniformity': max(0, min(1, uniformity))
            }
    
    return results

keys = [f"key_{i}" for i in range(1000)]
m_values = [50, 97, 200, 511]
A_values = [0.618033988749895, 0.5, 0.382, 0.75]

results = analyze_parameters(keys, m_values, A_values)

print("Parameter Analysis - Multiplicative Hashing")
print("m\tA\t\tVariance\tCollisions\tUniformity")
for (m, A), data in sorted(results.items()):
    print(f"{m}\t{A:.3f}\t\t{data['variance']:.2f}\t\t{data['collisions']}\t\t{data['uniformity']:.3f}")

best = min(results.items(), key=lambda x: x[1]['variance'])
print(f"\nBest parameters: m={best[0][0]}, A={best[0][1]:.3f}")
print(f"Variance: {best[1]['variance']:.2f}, Collisions: {best[1]['collisions']}, Uniformity: {best[1]['uniformity']:.3f}")
