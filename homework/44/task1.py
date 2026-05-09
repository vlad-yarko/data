def count_vowels(s):
    return sum(1 for c in s if c in 'aeiou')

print(count_vowels("hello world"))
