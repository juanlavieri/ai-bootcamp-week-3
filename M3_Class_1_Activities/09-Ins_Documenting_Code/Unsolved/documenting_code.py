def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers in the list.

    Raises:
        TypeError: If the argument is not a list.

    Examples:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([10, 20, 30])
        20.0
        >>> calculate_average([])
        0.0

    Note:
        This function uses the built-in `sum` function to calculate the sum of the numbers in the list,
        and then divides by the length of the list to get the average. If the list is empty, the function
        returns 0.0 to avoid a division by zero error.
    """
    if not isinstance(numbers, list):
        raise TypeError("Argument must be a list.")
    if len(numbers) == 0:
        return 0.0
    return sum(numbers) / len(numbers)
