"""Refactoring Examples"""


# Code using for loop.
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)

# Refactored the code to use a list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

# Code that uses the range() function.
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(f"The square of {numbers[i]} is {numbers[i]**2}")

# Refactored the code to use enumerate()
numbers = [1, 2, 3, 4, 5]
for i, num in enumerate(numbers):
    print(f"The square of {num} is {num**2}")

# Code without a function.
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    if num % 2 == 0:
        squares.append(num ** 2)
print(squares)

# Refactored code with a function
def get_even_squares(numbers):
    return [num ** 2 for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5]
squares = get_even_squares(numbers)
print(squares)

