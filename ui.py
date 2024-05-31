from calendar import Calendar
from event import Event
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
            command = input()
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
            print("Not enough data")
        else:
            datetime_from = utils.parse_date_str(" ".join(split[2:4]))
            datetime_to = utils.parse_date_str(" ".join(split[4:6]))

            name = ' '.join(split[5:])
            event = Event(datetime_from, datetime_to, name)

            cur_calendar.add_event(event)
            utils.save_calendar(cur_calendar, "calendar.csv")

            print("Event added")
    elif command.startswith("show week"):
        split = command.split(" ")

        date = utils.parse_date_str(split[2])

        utils.print_list(cur_calendar.generate_week_lines(date))
    elif command == "exit":
        sys.exit()
    else:
        print("Unknown command")
