def average(*nums):
    if not nums:
        return 0
    return sum(nums)/len(nums)

print(average(1,2,3))
print(average())
print(average(10))

# T2
letters = ["a", "bb", "ccc", "dd"]
lengths = [word for word in letters if len(word) > 1 ]
print(lengths)

num = [1, 2, 3]
squared = {n: n**2 for n in num}
print(squared)

def only_even(nums: list[int]) -> list[int]:
    return [n for n in nums if n % 2 == 0]

print(only_even([1, 2, 3, 4, 5, 6]))

# T3
def is_palindrome(s: str) -> bool:
    clean = s.replace(" ", "").lower()
    return clean == clean[::-1]

print(is_palindrome("Racecar"))      # True
print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("hello"))        # False

# T4
def read_numbers(path: str) -> list[int]:
    result = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    result.append(int(line))
                except ValueError:
                    pass
    except FileNotFoundError:
        return []
    return result

print(read_numbers("t4test.txt"))        # [10, 20, 30]
print(read_numbers("numbers2.txt"))       # [5, 7, -3, 100]
print(read_numbers("no_such_file.txt"))   # []