# This is a comment

"""
This is a
multi-line comment
"""

#Variables stores a value in memory

name = "Hammas"
age = 18

#Data Types Numeric: int, float, complex etc

x = 10       # int
y = 3.14     # float
z = 2 + 3j   # complex
is_active = True  # bool

#Type Casting Converting between types:

int(), float(), str(), bool(), list(), tuple()

x = "10"
y = int(x)     # string -> integer
z = float(x)   # string -> float
print(y, z)


#Input / Output Input from user: input() (always returns a string)

name = input("Enter your name: ")  # User input
age = int(input("Enter your age: "))  # Convert input to integer
print("Hello", name, "Your age is", age)


#Operators Arithmetic: +, -, *, /, %, ** (power), // (floor division)

a = 5
b = 3
print(a + b)  # 8
print(a > b)  # True
print(a == b or a > b)  # True


#Control Flow (Conditions & Loops)

if age >= 18:
    print("Adult")
elif age > 12:
    print("Teen")
else:
    print("Child")

#Data Structures List: Ordered, mutable

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
