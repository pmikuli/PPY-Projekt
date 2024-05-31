from calendar import Calendar
from event import Event
from typing import List
import datetime
import utils
import sys

cur_calendar = Calendar([])


def start_main_loop():
    global cur_calendar
    cur_calendar = utils.load_calendar("calendar.csv")
    execute("show today")

    try:
        while True:
            print("Enter command:")
            command = input("> ")
            execute(command)
    except KeyboardInterrupt:
        print("Exiting...")


def execute(command: str):
    command = command.strip().lower()
    if command == "show today":
        utils.print_list(cur_calendar.generate_day_lines(datetime.datetime.now()))
    elif command == "show this month":
        utils.print_list(cur_calendar.generate_month(datetime.datetime.now()))
    elif command == "show this week":
        utils.print_list(cur_calendar.generate_week_lines(datetime.datetime.now()))
    elif command.startswith("add event"):
        split = command.split(" ")
        if len(split) <= 6:
            print("Too few arguments")
        else:
            event = get_event_from_command(split[2:])

            cur_calendar.add_event(event)
            utils.save_calendar(cur_calendar, "calendar.csv")

            print("Event added")
    elif command.startswith("show week"):
        split = command.split(" ")
        if len(split) < 3:
            print("Too few arguments")
        else:
            date = utils.parse_date_str(split[2])

            utils.print_list(cur_calendar.generate_week_lines(date))
    elif command.startswith("show day "):
        date = utils.parse_date_str(command.split(" ")[2])
        utils.print_list(cur_calendar.generate_day_lines(date))
    elif command.startswith("show month"):
        split = command.split(" ")
        if len(split) < 4:
            print("Too few arguments")
        else:
            month = split[2]
            year = int(split[3])
            month = utils.convert_month_to_num(month)

            date = datetime.datetime(year, month, day=1)

            utils.print_list(cur_calendar.generate_month(date))
    elif command.startswith("remove event"):
        split = command.split(" ")
        if len(split) <= 6:
            print("Too few arguments")
        else:
            event = get_event_from_command(split[2:])
            cur_calendar.remove_event(event)

            utils.save_calendar(cur_calendar, "calendar.csv")

            print("Event removed")
    elif command == "exit":
        sys.exit()
    else:
        print("Unknown command")


def get_event_from_command(split: List[str]) -> Event:
    datetime_from = utils.parse_date_str(" ".join(split[0:2]))
    datetime_to = utils.parse_date_str(" ".join(split[2:4]))

    name = ' '.join(split[4:])
    return Event(datetime_from, datetime_to, name)
