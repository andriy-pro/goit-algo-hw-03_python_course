import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number to a standard format by removing all non-essential
    characters and ensuring it has the correct international prefix.

    Args:
    phone_number (str): A string containing the phone number in various formats.

    Returns:
    str: The normalized phone number.
    """
    # Strip and remove all non-digit characters except for the '+' sign
    cleaned_number = re.sub(r"[^\d+]", "", phone_number.strip())

    # Add '+' if necessary and handle '380' prefix correctly
    if not cleaned_number.startswith('+'):
        # Check if the number starts with '00' followed by a non-zero digit,
        # indicating another format of international phone number
        if cleaned_number.startswith('00') and cleaned_number[2] != '0':
            cleaned_number = '+' + cleaned_number[2:]
        elif cleaned_number.startswith('380'):
            cleaned_number = "+" + cleaned_number
        else:
            cleaned_number = "+380" + cleaned_number.lstrip("0")

    return cleaned_number
