# class Rectangle:
#     def __init__(self, width, height):
#         self.height = height
#         self.width = width

#     def area(self) -> int:
#         return self.height*self.width

#     def perimeter(self) -> int:
#         return 2*(self.height + self.width)

#     def __str__(self) -> str:
#         return f"Rectangle({self.width}x{self.height})"

#     def __repr__(self) -> str:
#         return f"Rectangle(width={self.width}, height={self.height})"
    
# # r = Rectangle(3, 4)
# # print(r.area(), r.perimeter())  # 12 14

# class Counter:
#     def __init__(self):
#         self.value = 0

#     def increment(self) -> None:
#         self.value += 1

#     def decrement(self) -> None:
#         if self.value == 0:
#             raise ValueError("Counter can't go below zero")
#         self.value -= 1

#     def reset(self) -> None:
#         self.value = 0

# # c = Counter()
# # c.increment()
# # c.increment()
# # print(c.value)  # 2
# # c.reset()
# # print(c.value)  # 0
# # c.decrement()   # ValueError

# # print(Rectangle(3, 4))    # Rectangle(3x4)
# # print([Rectangle(1, 2)])  # [Rectangle(width=1, height=2)]


# class Account:
#     def __init__(self, balance: int):
#         self._balance = balance

#     @property
#     def balance(self) -> int:
#         return self._balance

#     def deposit(self, amount: int) -> None:
#         if amount <= 0:
#             raise ValueError("Inappropriate value")
#         self._balance += amount

#     def withdraw(self, amount: int) -> None:
#         if amount <= 0 or amount > self._balance:
#             raise ValueError("Inappropriate value")
#         self._balance -= amount

# # acc = Account(100)
# # acc.deposit(50)
# # acc.withdraw(30)
# # print(acc.balance)  # 120
# # acc.withdraw(500)   # ValueError

# import math

# class Shape:
#     def area(self) -> float:
#         return 0

# class Circle(Shape):
#     def __init__(self, radius:float):
#         self.radius = radius

#     def area(self) -> float:
#         return math.pi * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side:float):
#         self.side = side

#     def area(self) -> float:
#         return self.side ** 2

# shapes = [Circle(1), Square(2), Shape()]
# for s in shapes:
#     print(round(s.area(), 2))  # 3.14, 4, 0

# class SavingsAccount(Account):
#     def __init__(self, balance: int, rate:float):
#         super().__init__(balance)
#         self.rate = rate

#     def add_interest(self) -> None:
#         self._balance += self.balance * self.rate / 100

# s = SavingsAccount(1000, 5)
# s.add_interest()
# print(s.balance)  # 1050.0

from dataclasses import dataclass, field, asdict

@dataclass
class Note:
    id: int
    title: str
    text: str = ""
    tags: list[str] = field(default_factory = list)

n = Note(1, "Первая")
print(n)                              # Note(id=1, title='Первая', text='', tags=[])
print(Note(1, "A") == Note(1, "A"))   # True
print(asdict(n))                      # {'id': 1, 'title': 'Первая', 'text': '', 'tags': []}

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    age: int = 18

class UserStorage:
    def __init__(self):
        self._users: dict[int, User] = {}

    def add(self, user: User) -> None:
        if user.id in self._users:
            raise ValueError("ID already exists")
        self._users[user.id] = user

    def get(self, user_id: int) -> User|None:
        return self._users.get(user_id)

    def delete(self, user_id: int) -> None:
        del self._users[user_id]

    def all(self) -> list[User]:
        return list(self._users.values())

    def adults(self) -> list[User]:
        return [user for user in self._users.values() if user.age >= 18]

# s = UserStorage()
# s.add(User(1, "Али", 20))
# s.add(User(2, "Дана", 16))
# print(s.get(1))          # User(id=1, name='Али', age=20)
# print(s.get(99))         # None
# print(s.adults())        # [User(id=1, name='Али', age=20)]
# s.delete(2)
# print(len(s.all()))      # 1
# s.add(User(1, "Дубль"))  # ValueError