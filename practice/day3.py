class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
            return f"Hi, I'm {self.name}"

    def birthday(self) -> None:
         self.age += 1

    # 2
    def __str__(self) -> str:
         return f"User({self.name}, {self.age})"
    # 3
    def __repr__(self) -> str:
         return f"User(name = {self.name!r}, age={self.age})"

# u = User("Ali", 20)
# print(u.greet())
# u.birthday()
# print(u.age)

print([User("Ali", 20)])

class Account:
    def __init__(self, balance: int):
          self._balance = balance

    def deposit(self, amount: int) -> None:
     if amount <= 0:
          raise ValueError("The sum should be positive")
     self._balance += amount

    def get_balance(self) -> int:
         return self._balance

    @property
    def balance(self) -> int:  
        return self._balance

acc = Account(100)
acc.deposit(50)
print(acc.balance)
