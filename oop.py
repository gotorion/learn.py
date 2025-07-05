from enum import Enum
class ATM:
    def __init__(self, number, money):
        self.number = number
        self.money = money

    def add(self, money):
        self.money += money

    def show_money(self):
        print(self.money)


atm1 = ATM(10, 100)
atm1.show_money()

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Cat:
    def __init__(self, cat_name, age, color):
        self.name = cat_name
        self.age = age
        self.color = color

    def speak(self):
        print(f"My name is " + self.name)
        print(f"My color is {self.color}")

my_cat = Cat("Tom", 3, Color.RED)
print(my_cat.name)
print(f"My cat name is {my_cat.name}")

my_cat.speak()