from datetime import datetime


def calculate_age(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y/%m/%d")
        current_date = datetime.now()

        age = current_date.year - birth_date.year
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            age -= 1

        return str(age)
    except ValueError:
        return "WRONG"


date_str = input().strip()
print(calculate_age(date_str))