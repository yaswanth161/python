def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
def find_anniversary(date):
    day, month, year = map(int, date.split('/'))
    is_leap = is_leap_year(year)
    if is_leap:
        next_anniversary = f"{day}/{month}/{year + 1}"
        print(f"Given Anniversary Year: Leap Year. Next Anniversary Date: {next_anniversary}")
    else:
        previous_anniversary = f"{day}/{month}/{year - 1}"
        print(f"Given Anniversary Year: Non Leap Year. Previous Anniversary Date: {previous_anniversary}")
date = input("Enter Date (DD/MM/YYYY): ")
find_anniversary(date)
