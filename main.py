# 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Salom, men {self.name}"

p1 = Person("Ali", 20)


# 2
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} - {self.year}"

c1 = Car("BMW", 2022)


# 3
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Vali")


# 4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r1 = Rectangle(5, 10)


# 5
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)

