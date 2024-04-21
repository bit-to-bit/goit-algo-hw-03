'''Tests'''
import utils

# Test 01: get_days_from_today()
print("\nTest 01: get_days_from_today()\n" + "-"*50)

test_days = ["2024-04-28", "2024-04-20", "2024-04-21", "2024-04-22"]

for test_date in test_days:
    print(test_date, " days ->", utils.get_days_from_today(test_date))

# Test 02: get_numbers_ticket()
print("\nTest 02: get_numbers_ticket()\n" + "-"*50)
print(utils.get_numbers_ticket(1,1000,10))
print(utils.get_numbers_ticket(2,3,2))
print(utils.get_numbers_ticket(1,1,1))
print(utils.get_numbers_ticket(1,12000,10))
print(utils.get_numbers_ticket(1,10,10))
print(utils.get_numbers_ticket(1,10,11))

# Test 03: utils.normalize_phone()
print("\nTest 03: normalize_phone()\n" + "-"*50)

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

sanitized_numbers = [utils.normalize_phone(num) for num in raw_numbers]
for phone_number in sanitized_numbers:
    print(phone_number)

# Test 04: utils.get_upcoming_birthdays()
print("\nTest 04: get_upcoming_birthdays()\n" + "-"*50)

users = [
    {"name": "John 1985.03.23", "birthday": "1985.03.23"},
    {"name": "John 1985.04.19", "birthday": "1985.04.19"},
    {"name": "John 1985.04.20", "birthday": "1985.04.20"},
    {"name": "John 1985.04.21", "birthday": "1985.04.21"},
    {"name": "John 1985.04.22", "birthday": "1985.04.22"},
    {"name": "John 1985.04.23", "birthday": "1985.04.23"},
    {"name": "John 1985.04.26", "birthday": "1985.04.26"},
    {"name": "Jane 1990.04.27", "birthday": "1990.04.27"},
    {"name": "John 1985.04.28", "birthday": "1985.04.28"}
]

upcoming_birthdays = utils.get_upcoming_birthdays(users)
for user in upcoming_birthdays:
    print(user)
