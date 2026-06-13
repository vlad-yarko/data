import time

def boyer_moore_search(text, pattern):
    if not pattern or not text:
        return -1
    
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    
    i = len(pattern) - 1
    j = len(pattern) - 1
    
    while i < len(text):
        if pattern[j] == text[i]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        else:
            shift = bad_char.get(text[i], -1)
            i += len(pattern) - min(j, shift + 1)
            j = len(pattern) - 1
    
    return -1

text_short = "ABCCDDAEFGAHIAJAK" * 10
pattern_short = "AAAB"

text_long = "the quick brown fox jumps over the lazy dog " * 1000
pattern_long = "lazy dog"

start = time.time()
bm_result = boyer_moore_search(text_short, pattern_short)
t_bm_short = time.time() - start

start = time.time()
find_result = text_short.find(pattern_short)
t_find_short = time.time() - start

print(f"Short text - Boyer-Moore: index {bm_result}, time {t_bm_short:.6f}s")
print(f"Short text - str.find: index {find_result}, time {t_find_short:.6f}s")

start = time.time()
bm_result = boyer_moore_search(text_long, pattern_long)
t_bm_long = time.time() - start

start = time.time()
find_result = text_long.find(pattern_long)
t_find_long = time.time() - start

print(f"Long text - Boyer-Moore: index {bm_result}, time {t_bm_long:.6f}s")
print(f"Long text - str.find: index {find_result}, time {t_find_long:.6f}s")
