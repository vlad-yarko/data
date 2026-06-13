def find_last_occurrence(text, sub):
    return text.rfind(sub)

def index_last_occurrence(text, sub):
    try:
        return text.rindex(sub)
    except ValueError:
        return -1

text1 = "hello world, hello universe, hello"
text2 = "goodbye world"

print(f"rfind in '{text1}' for 'hello': {find_last_occurrence(text1, 'hello')}")
print(f"rindex in '{text1}' for 'hello': {index_last_occurrence(text1, 'hello')}")

print(f"rfind in '{text2}' for 'hello': {find_last_occurrence(text2, 'hello')}")
print(f"rindex in '{text2}' for 'hello': {index_last_occurrence(text2, 'hello')}")

print(f"rfind in '{text1}' for 'world': {find_last_occurrence(text1, 'world')}")
print(f"rindex in '{text1}' for 'world': {index_last_occurrence(text1, 'world')}")
