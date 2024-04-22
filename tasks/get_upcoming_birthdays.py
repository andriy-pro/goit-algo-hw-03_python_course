from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    """
    Get upcoming birthdays within the next 7 days for users.

    Args:
    users (list): A list of dictionaries containing user information including name and birthday.

    Returns:
    list: A list of dictionaries containing user names and the date of congratulation for their
          upcoming birthdays.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Parse the birthday and adjust the year part
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)


        # If the birthday has already passed this year, we'll consider the date for the next year,
        # as stated in condition №4 in the task description,
        # although I personally don't find this requirement necessary.
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the day difference to see if within the next 7 days
        day_difference = (birthday_this_year - today).days
        if 0 <= day_difference <= 7:
            # Adjust for weekends
            if birthday_this_year.weekday() > 4:  # If Saturday (5) or Sunday (6)
                congratulation_date = birthday_this_year + \
                                      + timedelta(days= 7 - birthday_this_year.weekday() )
            else:
                congratulation_date = birthday_this_year

            # Append the result to the list with formatted date
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
