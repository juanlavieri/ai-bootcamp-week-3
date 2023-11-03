"""Pizza Order"""

def create_pizza_order():
    """
    This function allows the user to create a pizza order by selecting three toppings from a list of five options.
    The function prompts the user to enter the number of their chosen topping and validates the input.
    The function then prints the selected toppings as the order.

    Args:
    None

    Returns:
    None

    Raises:
    ValueError: If the user enters an invalid topping number.
    """
    # Prompt the user to select three toppings from a list of five options
    toppings = ['pepperoni', 'mushrooms', 'onions', 'sausage', 'bell peppers']

    print("Welcome to the Sal's Famous Pizza!")
    print("Please choose three toppings for your pizza from the following options:")

    # Display the list of toppings to the user
    for i, topping in enumerate(toppings, start=1):
        print(f"{i}. {topping}")

    selected_toppings = []
    for _ in range(3):
        # Prompt the user to enter the number of their chosen topping
        topping_number = int(input("Enter the number of your chosen topping: "))

        # Validate the user's input
        while topping_number < 1 or topping_number > 5:
            print("Invalid topping number. Please try again.")
            topping_number = int(input("Enter the number of your chosen topping: "))

        # Add the selected topping to the list of toppings
        selected_toppings.append(toppings[topping_number - 1])

    # Print the selected toppings as the order
    print("Here is your order:")
    print("Your pizza comes with:", ", ".join(selected_toppings))

if __name__ == "__main__":
    create_pizza_order()
