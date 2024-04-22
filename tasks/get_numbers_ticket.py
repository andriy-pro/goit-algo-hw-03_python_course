import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """
    Generate a list of unique random numbers within the specified range.

    Args:
    min_num (int): The minimum possible number in the range.
    max_num (int): The maximum possible number in the range.
    quantity (int): The number of unique random numbers to select.

    Returns:
    list: A sorted list of unique random numbers within the specified range.

    Raises:
    ValueError: If the input values are incorrect, an empty list is returned, as per the task instructions.
    """

    try:
        if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
            raise ValueError

    except ValueError:
        # In case of incorrect values, an empty list is returned, as specified in the task requirements.
        return []

    random_numbers = random.sample(range(min_num, max_num + 1), quantity)

    return sorted(random_numbers)
