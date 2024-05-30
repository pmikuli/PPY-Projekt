from typing import List

def save_calendar(calendar, filename):
    raise NotImplemented


def load_calendar(filename):
    raise NotImplemented


def are_days_equal(date1, date2):
    return (date1.day == date2.day
            and date1.month == date2.month
            and date1.year == date2.year)

def print_list(list: List):
    for i in list:
        print(i)