# T1
def count_words(text: str) -> dict:
    d = {}
    clean = text.split()
    for word in clean:
       d[word] = d.get(word, 0) + 1
    return d

# T2
def find_duplicates(nums: list[int]) -> list[int]:
    d = {}
    result = []
    for n in nums:
        d[n] = d.get(n, 0) + 1
    for key, count in d.items():
        if count > 1:
            result.append(key)
    return result

# T3
def only_even(nums: list[int]) -> list[int]:
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result

# T4
def most_common(items: list) -> object:
    d = {}
    for item in items:
        d[item] = d.get(item, 0) + 1

    best_item = None
    best_count = 0
    for key, count in d.items():
        if best_count < count:
            best_count = count
            best_item = key
    return best_item

# T5
def invert(d: dict) -> dict:
    result = {}
    for key, value in d.items():
        result[value] = key
    return result

print(invert({"a": 1, "b": 2}))  # {1: "a", 2: "b"}
print(invert({}))                # {}
print(invert({"x": 10}))         # {10: "x"}