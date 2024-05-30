from calendar import Calendar
from event import Event
import datetime

def main():
    event = Event(datetime.datetime.now(), datetime.datetime.now(), "First event")
    another_event = Event(datetime.datetime.now(), datetime.datetime.now(), "An event with a very, very long name sdfgjdflgkj;sdkgs ;dlkgj sdf;klgjs;ldfkgjs;dfklgjs;dlfkgjs;dfklgjs;dfkgjsdl;fkgjk;sdfglk")
    events = [event, another_event]
    cal = Calendar(events)
    cal.print_day(datetime.datetime.now())
    cal.print_week(datetime.datetime.now())
    print()
    cal.print_month(datetime.datetime.now())


if __name__ == "__main__":
    main()