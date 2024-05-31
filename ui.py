from calendar import Calendar
from event import Event
from typing import List
import datetime
import utils
import sys
import calendar_view as view

cur_calendar = Calendar([])
path = "calendar.csv"


def start_main_loop():
    global cur_calendar
    cur_calendar = utils.load_calendar(path)
    execute("show today")

    while True:
        try:
            print("Enter command:")
            command = input("> ")
            execute(command)
        except KeyboardInterrupt:
            print("Exiting...")
        except Exception as e:
            print("Error when executing command: ", e)


def execute(command: str):
    command = command.strip().lower()
    if command == "show today":
        utils.print_list(view.generate_day_lines(cur_calendar, datetime.datetime.now()))
    elif command == "show this month":
        utils.print_list(view.generate_month(cur_calendar, datetime.datetime.now()))
    elif command == "show this week":
        utils.print_list(view.generate_week_lines(cur_calendar, datetime.datetime.now()))
    elif command.startswith("add event"):
        split = command.split(" ")
        if len(split) <= 6:
            print("Too few arguments")
        else:
            event = get_event_from_command(split[2:])

            cur_calendar.add_event(event)
            utils.save_calendar(cur_calendar, path)

            print("Event added")
            utils.print_list(view.generate_day_lines(cur_calendar, event.date_from))
    elif command.startswith("show week"):
        split = command.split(" ")
        if len(split) < 3:
            print("Too few arguments")
        else:
            date = utils.parse_date_str(split[2])

            utils.print_list(view.generate_week_lines(cur_calendar, date))
    elif command.startswith("show day "):
        date = utils.parse_date_str(command.split(" ")[2])
        utils.print_list(view.generate_day_lines(cur_calendar, date))
    elif command.startswith("show month"):
        split = command.split(" ")
        if len(split) < 4:
            print("Too few arguments")
        else:
            month = split[2]
            year = int(split[3])
            month = utils.convert_month_to_num(month)

            date = datetime.datetime(year, month, day=1)

            utils.print_list(view.generate_month(cur_calendar, date))
    elif command.startswith("remove event"):
        split = command.split(" ")
        if len(split) <= 6:
            print("Too few arguments")
        else:
            event = get_event_from_command(split[2:])
            cur_calendar.remove_event(event)

            utils.save_calendar(cur_calendar, path)

            print("Event removed")
            utils.print_list(view.generate_day_lines(cur_calendar, event.date_from))
    elif command == "exit":
        sys.exit()
    else:
        print("Unknown command")


def get_event_from_command(split: List[str]) -> Event:
    datetime_from = utils.parse_date_str(" ".join(split[0:2]))
    datetime_to = utils.parse_date_str(" ".join(split[2:4]))

    name = ' '.join(split[4:])
    return Event(datetime_from, datetime_to, name)
