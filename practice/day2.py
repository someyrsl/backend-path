def total(*args):
    return sum(args)

print(total(2,3,4))
print(total(2))

def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# show(name = "Axellov", age = 20)

def log(level,*args, **kwargs):
    print(level, args, kwargs)

log("INFO", 1, 2, user = "bob")

def greet(name: str, greeting: str = "Привет") -> str:
    return f"{greeting}, {name}"

# print(greet(name = "Yerassyl", greeting = "Hello"))
# print(greet("Ali"))

# List Comprehension
nums = [1,2,3,4,5,6]
squares = [n *n for n in nums] # [1, 4, 9, 16, 25, 36]
evens = [n for n in nums if n % 2 == 0]      # [2, 4, 6]

# Dict Comprehension
words = ["apple", "kiwi", "banana"]
lengths = {w: len(w) for w in words} # {"apple": 5, "kiwi": 4, "banana": 6}

# Set Comprehension
unique = {n % 3 for n in nums} # {0, 1, 2}

# Строки
s = "  Hello,  Backend  "
print(s.strip())
print(s.lower(), s.upper())
print(s.replace("Hello", "Hi"))
print("a,b,c".split(","))
print("-".join(["a", "b", "c"]))

s = "backend"
print(s.startswith("back"), s.endswith("end"), "ken" in s)
print("123".isdigit(), "abc".isalpha())

print(s[0], s[-1], s[1:4],  s[::-1])

price = 1234.5
print(f"Price: {price:.2f}")

# Files
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("первая строка\n")
    f.write("вторая строка\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)

with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Exceptions
try:
    n = int("abc")
except ValueError:
    print("Не число")

try:
    open("no_such_file.txt")
except FileNotFoundError:
    print("Файла нет")

try:
    x = 10 / int(input("Делитель: "))
except ZeroDivisionError:
    print("На ноль делить нельзя")
except ValueError:
    print("Введи число")
else:
    print("Результат:", x)
finally:
    print("Выполнится всегда")

# Raise
def set_age(age: int) -> int:
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    return age