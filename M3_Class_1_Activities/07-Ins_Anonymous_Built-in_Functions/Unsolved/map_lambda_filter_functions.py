# Anonymous Functions
def divide_by_seven(num):
    return num / 7

# 1. A function that divides by 7 and rounds to the nearest hundredth
def divide_by_seven_round(num):
    return round(num / 7, 2)

# 2. Create a list comprehension that divides by 7 and rounds to the nearest hundredth
lst = [round(num / 7, 2) for num in range(1, 101)]
print(lst)
# 3. Instead of using a list comprehension we can use the map function to do the same thing.
lst = list(map(lambda num: round(num / 7, 2), range(1, 101)))
print(lst)
# 4. Demonstrate how to implement the previous example as a lambda function within the map function
lst = list(map(lambda num: round(divide_by_seven(num), 2), range(1, 101)))
print(lst)
# 5. Use the filter and lambda functions to get only the numbers divided by 3.
lst = list(filter(lambda num: num % 3 == 0, range(1, 101)))
print(lst)