import math as m

def main():
    """
    This function demonstrates how to import modules, functions and methods in Python.
    """
    # Import the sqrt function from the math module.
    print(m.sqrt(4))    # 2.0   # Use the alias to access the function

    # Calculate the square root of a number.
    def sqrt(num):
        """
        This function calculates the square root of a number.
        """
        return num ** 0.5

    # Import the randint and choice methods from the random module.
    from random import randint, choice
    print(randint(1, 10))    # 8    # Use the function name to access the method

    # Generate a random number between 1 and 10 and selecting a random element from a list.
    my_list = [1, 2, 3, 4, 5]
    random_num = randint(1, 10)

    # Use the choice method to randomly select an element from the list.
    random_element = choice(my_list)

    # Import the datetime and date classes from the datetime module.
    from datetime import datetime, date

    # Get the current datetime using the now function.
    current_datetime = datetime.now()

    # Get the current time using the strftime function.
    current_time = current_datetime.strftime("%H:%M:%S")

    # Get the current date using the today function.
    current_date = date.today()

    # Print the results
    print(f"The square root of 4 is {m.sqrt(4)}")
    print(f"A random number between 1 and 10 is {random_num}")
    print(f"A random element from the list {my_list} is {random_element}")
    print(f"The current datetime is {current_datetime}")
    print(f"The current time is {current_time}")
    print(f"The current date is {current_date}")
if __name__ == "__main__":
    main()
