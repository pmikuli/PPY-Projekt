#!/usr/bin/env python3

from calendar import Calendar
from event import Event
from typing import List
import datetime
import utils
import sys
import calendar_view as view
from pathlib import Path


cur_calendar = Calendar([])
path = str(Path.home()) + "/calendar.csv"


def main():
    if len(sys.argv) == 2:
        global path
        path = sys.argv[1]
    __start_main_loop()


def __start_main_loop():
    global cur_calendar
    cur_calendar = utils.load_calendar(path)
    __execute("show today")

    while True:
        try:
            print("Enter command:")
            command = input("> ")
            __execute(command)
        except KeyboardInterrupt:
            print("Exiting...")
            return
        except Exception as e:
            print("Error when executing command: ", e)


def __execute(command: str):
    command = command.strip().lower()
    if command == "show today":
        view.print_day(cur_calendar, datetime.datetime.now())
    elif command == "show this month":
        view.print_month(datetime.datetime.now())
    elif command == "show this week":
        view.print_week(cur_calendar, datetime.datetime.now())
    elif command.startswith("add event"):
        split = command.split(" ")
        if len(split) <= 6:
            print("Too few arguments")
        else:
            event = __get_event_from_command_args(split[2:])

            cur_calendar.add_event(event)
            utils.save_calendar(cur_calendar, path)

            print("Event added")
            view.print_day(cur_calendar, event.date_from)
    elif command.startswith("show week"):
        split = command.split(" ")
        if len(split) < 3:
            print("Too few arguments")
        else:
            date = utils.parse_date_str(split[2])

            utils.print_list(view.__generate_week_lines(cur_calendar, date))
    elif command.startswith("show day "):
        date = utils.parse_date_str(command.split(" ")[2])
        view.print_day(cur_calendar, date)
    elif command.startswith("show month"):
        split = command.split(" ")
        if len(split) < 4:
            print("Too few arguments")
        else:
            month = split[2]
            year = int(split[3])
            month = utils.convert_month_to_num(month)

            date = datetime.datetime(year, month, day=1)

            view.print_month(date)
    elif command.startswith("remove event"):
        split = command.split(" ")
        if len(split) <= 6:
            print("Too few arguments")
        else:
            event = __get_event_from_command_args(split[2:])
            cur_calendar.remove_event(event)

            utils.save_calendar(cur_calendar, path)

            print("Event removed")
            view.print_day(cur_calendar, event.date_from)
    elif command == "help":
        print('''Available commands::
- `show today` - shows the day view for today.
- `show this month` - shows the month view for today.
- `show this week` - shows the week view for today. The week view shows all the events throughout the week.
- `add event DATE_FROM DATE_TO EVENT_DESCRIPTION` - accepts 3 positional arguments: DATE_FROM, DATE_TO and EVENT_DESCRIPTION. The dates should be in format `dd-mm-yyyy HH:MM`. Adds an event to the calendar using given information. 
- `remove event DATE_FROM DATE_TO EVENT_DESCRIPTION` - use in a similar fashion as the command above. Removes an event from the calendar.
- `show day DATE` - Accepts one argument which is the day for which to display the day view. The given date should be formatted as `dd-mm-yyyy`. 
- `show week DATE`- same as above, but shows the week view for the given day.
- `show month MONTH_NAME YEAR` - accepts 2 arguments: the name of the month and year. The name should be a full name, for example: "Decemeber".
- `help`- lists commands and their descriptions.
- `exit` - closes the application and saves calendar to a file. ''')
    elif command == "exit":
        sys.exit()
    else:
        print("Unknown command")


def __get_event_from_command_args(split: List[str]) -> Event:
    datetime_from = utils.parse_date_str(" ".join(split[0:2]))
    datetime_to = utils.parse_date_str(" ".join(split[2:4]))

    name = ' '.join(split[4:])
    return Event(datetime_from, datetime_to, name)


if __name__ == "__main__":
    main()
