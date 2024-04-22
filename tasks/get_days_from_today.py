from datetime import datetime, date


def get_days_from_today(input_date_string: str) -> int:
    """
    Calculate the number of days from the given date to today's date.
    
    Args:
    input_date_string (str): A string representing a date in the format 'YYYY-MM-DD'.
    
    Returns:
    int: The number of days from the given date to today. Positive if the 
        given date is in the future, negative if it is in the past.
         
    Raises:
    ValueError: If the 'input_date_string' is not in the correct format.
    """
    try:
        # Convert the string to a datetime.date object
        target_date = datetime.strptime(input_date_string, "%Y-%m-%d").date()

        # Get today's date (only the date, not datetime)
        today_date = date.today()

        # Calculate and return the difference in days
        return (target_date - today_date).days

    except ValueError as err:
        raise ValueError("The date format should be YYYY-MM-DD") from err
