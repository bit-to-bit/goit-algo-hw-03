'''Module providing the util functions'''
from datetime import datetime

def get_days_from_today(date: str) -> int:
    '''Returns the number of days between the current date and the given date'''

    try:
        given = datetime.strptime(date, "%Y-%m-%d")
    except (ValueError, TypeError) as e:
        print(f"The date must be in the format YYYY-MM-DD: {e}")
        raise

    return (datetime.today() - given).days

print(get_days_from_today("2024-04-20"))
