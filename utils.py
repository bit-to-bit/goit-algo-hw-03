'''Module providing the util functions'''
from datetime import datetime
from datetime import timedelta
import random
import re

def get_days_from_today(date: str) -> int:
    '''Calculate the number of days between the current date and the given date

    Args:
        date (str): the date in format YYYY-MM-DD.

    Returns:
        number of days.

    Raises:
    TypeError: if date is not a str.
    ValueError: if date not in format YYYY-MM-DD.
    '''

    try:
        given = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as e:
        raise ValueError("The date should be in the format YYYY-MM-DD") from e

    return (datetime.today().date() - given).days

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    '''Generates a set of unique random numbers for a lottery ticket

    Args:
        min (int): the minimum possible number in the set (not less than 1).
        max (int): the maximum possible number in the set (not more than 1000).
        quantity (int): the number of numbers to be selected (a value between min and max).

    Returns:
        list of unique random numbers or empty list if parameters do not meet the restrictions.

    Raises:
    TypeError: if min, max, quantity are not a number.
    '''

    result_list = []
    if 0 < min <= max <= 1000 and quantity <= max - min + 1:
        numbers_list = list(range(min, max + 1))
        result_list = random.sample(numbers_list, quantity)
        result_list.sort()
    return result_list

def add_phone_country_code(phone_number: str) -> str:
    '''Add to phone number country code if need

    Args:
        phone_number (str): the phone number in format witn digits or symbol "+" only

    Returns:
        phone number wtih country code at the beginning.

    Raises:
    TypeError: if phone_number is not a str.
    '''

    pattern = r"^(\+{,1}380{,1}|0{,1})(\d*)"
    replacement = r"+380\2"
    result = re.sub(pattern, replacement, phone_number)
    return result

def normalize_phone(phone_number: str) -> list:
    '''Normalize phone number

    Args:
        phone_number (str): the phone number in format witn digits and symbol "+" only.

    Returns:
        list of phone numbers in format witn digits and symbol "+" at the beginning only.
    '''
    pattern = r"[^\d\+]"
    replacement = ""
    result = add_phone_country_code(re.sub(pattern, replacement, phone_number))
    return result

def get_greeting_tuple(birthday: str)  -> tuple:
    '''Calculate the user greeting date

    Args:
        birthday (str): the date in format YYYY.MM.DD.

    Returns:
        tuple in format (next_birthday_str, is_greet_this_week, greeting_date_str).

    Raises:
    TypeError: if birthday is not a str.
    ValueError: if birthday not in format YYYY.MM.DD.
    '''
    today = datetime.today().date()
    today_year, today_month, today_day = today.timetuple()[0:3]
    birthday = datetime.strptime(birthday, "%Y.%m.%d").date()
    birthday_month, birthday_day = birthday.timetuple()[1:3]
    next_birthday_year =  today_year + 1 if (today_month,today_day)  > (birthday_month,birthday_day) else today_year
    next_birthday =  datetime(next_birthday_year, birthday_month, birthday_day).date()
    next_monday = next_birthday + timedelta(days = 7 - next_birthday.weekday())
    is_greet_this_week = next_birthday - today <= timedelta(days=6)
    greeting_date = next_monday if next_birthday.isoweekday() in (6,7) else next_birthday
    next_birthday_str = datetime.strftime(next_birthday,"%Y.%m.%d")
    greeting_date_str = datetime.strftime(greeting_date,"%Y.%m.%d")
    return (next_birthday_str, is_greet_this_week, greeting_date_str)

def get_upcoming_birthdays(users: list)  -> list:
    '''Create a list of users to be congratulated on their birthday this week

    Args:
        users (list): users in format {"name": "user_name", "birthday": "YYYY.MM.DD"}.

    Returns:
        list of users to be congratulated on their birthday this week.
    '''

    greeting_list = []
    for user in users:
        is_greet_this_week, greeting_date = get_greeting_tuple(user["birthday"])[1:3]
        if is_greet_this_week:
            greeting_list.append({'name': user["name"], 'congratulation_date': greeting_date})
    return greeting_list
