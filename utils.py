from typing import List
from calendar import Calendar
from datetime import datetime
import event
import csv


def save_calendar(calendar: Calendar, filename: str):
    with open(filename, 'w') as f:
        w = csv.writer(f)
        for e in calendar:
            f.write(date_to_str(e.date_from) + "," + date_to_str(e.date_to) + "," + e.name + "\n")

def load_calendar(filename: str) -> Calendar:
    with open(filename, 'r') as f:
        events = []
        reader = csv.reader(f)
        for row in reader:
            date_from = parse_date_str(row[0])
            date_to = parse_date_str(row[1])
            events.append(event.Event(date_from, date_to, row[2]))
        calendar = Calendar(events)
        return calendar


def print_list(lines: List):
    for i in lines:
        print(i)


def parse_date_str(date_str: str) -> datetime:
    split = date_str.split(" ")

    d = split[0]

    day = int(d.split("-")[0])
    month = int(d.split("-")[1])
    year = int(d.split("-")[2])

    if len(split) == 2:
        t = split[1]

        hour = int(t.split(":")[0])
        minutes = int(t.split(":")[1])
        print(day)
        return datetime(year, month, day, hour, minutes)
    else:
        return datetime(year, month, day)


def date_to_str(date: datetime) -> str:
    return date.strftime("%d-%m-%Y %H:%M")


def convert_month_to_num(month: str) -> int:
    month = month.strip().lower()
    if month == "january":
        return 1
    elif month == "february":
        return 2
    elif month == "march":
        return 3
    elif month == "april":
        return 4
    elif month == "may":
        return 5
    elif month == "june":
        return 6
    elif month == "july":
        return 7
    elif month == "august":
        return 8
    elif month == "september":
        return 9
    elif month == "october":
        return 10
    elif month == "november":
        return 11
    elif month == "december":
        return 12
    else:
        return -1
