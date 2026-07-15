import math

def modular_hash(key, m):
    return hash(key) % m

def multiplicative_hash(key, m, A=0.618033988749895):
    h = hash(key)
    return int(m * ((A * h) % 1))

def analyze_hash_functions(keys, m):
    mod_hashes = [modular_hash(k, m) for k in keys]
    mult_hashes = [multiplicative_hash(k, m) for k in keys]
    
    mod_collisions = len(keys) - len(set(mod_hashes))
    mult_collisions = len(keys) - len(set(mult_hashes))
    
    mod_distribution = [0] * m
    mult_distribution = [0] * m
    
    for h in mod_hashes:
        mod_distribution[h] += 1
    for h in mult_hashes:
        mult_distribution[h] += 1
    
    mod_variance = sum((x - len(keys) / m) ** 2 for x in mod_distribution) / m
    mult_variance = sum((x - len(keys) / m) ** 2 for x in mult_distribution) / m
    
    return {
        'modular': {'collisions': mod_collisions, 'variance': mod_variance, 'distribution': mod_distribution},
        'multiplicative': {'collisions': mult_collisions, 'variance': mult_variance, 'distribution': mult_distribution}
    }

keys = [f"key_{i}" for i in range(1000)]
m = 97

results = analyze_hash_functions(keys, m)

print("Modular Hashing:")
print(f"  Collisions: {results['modular']['collisions']}")
print(f"  Variance: {results['modular']['variance']:.2f}")

print("\nMultiplicative Hashing:")
print(f"  Collisions: {results['multiplicative']['collisions']}")
print(f"  Variance: {results['multiplicative']['variance']:.2f}")

print("\nDistribution comparison:")
print(f"Modular - Min: {min(results['modular']['distribution'])}, Max: {max(results['modular']['distribution'])}")
print(f"Multiplicative - Min: {min(results['multiplicative']['distribution'])}, Max: {max(results['multiplicative']['distribution'])}")
