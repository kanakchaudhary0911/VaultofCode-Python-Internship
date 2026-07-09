"""
Assignment 1: Code Review and Error Correction
Python Programming Internship - VaultofCode

Prepared by: Kanak Chaudhary
"""

# -------------------------------------------------
# Code Snippet 1
# -------------------------------------------------

def add_numbers(a, b):
    return a + b

print("Snippet 1 Output:", add_numbers(5, 10))


# -------------------------------------------------
# Code Snippet 2
# -------------------------------------------------

name = "Alice"
print("Snippet 2 Output: Hello, " + name)


# -------------------------------------------------
# Code Snippet 3
# -------------------------------------------------

for i in range(5):
    print("Snippet 3 Output: Number:", i)


# -------------------------------------------------
# Code Snippet 4
# -------------------------------------------------

my_list = [1, 2, 3, 4, 5]
print("Snippet 4 Output: The fifth element is:", my_list[4])


# -------------------------------------------------
# Code Snippet 5
# -------------------------------------------------

def greet(name):
    print("Snippet 5 Output: Hello", name)

greet("Bob")


# -------------------------------------------------
# Code Snippet 6
# -------------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("Snippet 6 Output: You are eligible to vote.")
else:
    print("Snippet 6 Output: You are not eligible to vote.")


# -------------------------------------------------
# Code Snippet 7
# -------------------------------------------------

def multiply(a, b):
    result = a * b
    return result

print("Snippet 7 Output:", multiply(4, 5))


# -------------------------------------------------
# Code Snippet 8
# -------------------------------------------------

count = 10

while count > 0:
    print("Snippet 8 Output:", count)
    count -= 1

print("Snippet 8 Output: Countdown complete!")