import utils
from datetime import datetime
from datetime import timedelta
from event import Event
from typing import List


class Calendar:
    def __init__(self, events):
        self.events = events
        self.date_format = "%d-%m-%Y"

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.events):
            result = self.events[self.i]
            self.i += 1
            return result

        raise StopIteration

    def add_event(self, event: Event):
        self.events.append(event)
        # TODO add sorting events by date and time

    def print_month(self, date: datetime):
        print(date.strftime("%B"))

    def generate_week_lines(self, date: datetime):

        temp = []
        max_len = 0

        week_start = date - timedelta(days=date.weekday())
        for i in range(7):
            lines = self.generate_day_lines(week_start + timedelta(days=i), 40)
            max_len = max(max_len, len(lines))
            temp.append(lines)

        result = []
        for lines in temp:
            equalized = equalize_height(lines, max_len)
            for i in range(max_len):
                if i < len(result):
                    result[i] = result[i] + equalized[i]
                else:
                    result.append(equalized[i])
        return result

    def print_week(self, date: datetime):
        utils.print_list(self.generate_week_lines(date))

    def generate_day_lines(self, date: datetime, width=80) -> List[str]:
        result = []

        lines = []
        i = 1

        for event in self.events:
            if utils.are_days_equal(event.date_from, date) or utils.are_days_equal(event.date_to, date):
                line = (str(i) + ". " + event.date_from.strftime("%H:%M") + "-"
                        + event.date_to.strftime("%H:%M") + " " + event.name)

                if len(line) + 4 > width:
                    # save space for "|" at the beginning and end + space
                    chunk_size = width - len(str(i)) - 6
                    lines.append(fill(line[0:chunk_size + len(str(i))], width)) # doesn't require space
                    chunks = [line[i:i+chunk_size] for i in range(1, len(line), chunk_size)]
                    for c in chunks:
                        for _ in range(len(str(i)) + 2):
                            c = " " + c
                        lines.append(fill(c, width))
                else:
                    lines.append(fill(line, width))
                i += 1

        if len(lines) == 0:
            for i in range(3):
                lines.append(fill("", width))

        separator_line = ""
        for j in range(width):
            separator_line += "-"

        result.append(separator_line)

        # TODO extract to function
        day_of_the_week_line = date.strftime("%A")
        result.append(center(day_of_the_week_line, width))

        date_line = date.strftime(self.date_format)
        result.append(center(date_line, width))

        result.append(separator_line)
        for line in lines:
            result.append(line)
        result.append(separator_line)

        return result

    def print_day(self, date: datetime, width=80):
        utils.print_list(self.generate_day_lines(date, width))


# TODO move to utils

def center(text: str, width: int) -> str:
    len_text = len(text)
    n = width // 2 - len_text // 2 - 1
    for i in range(n):
        text = " " + text
    text = "|" + text
    for i in range(width - n - 2 - len_text):
        text = text + " "
    text = text + "|"

    return text

def fill(text: str, width: int) -> str:
    for i in range(width - len(text) - 4):
        text += " "
    return "| " + text + " |"


def equalize_height(lines: List[str], desired_len: int):
    if len(lines) < desired_len:
        diff = desired_len - len(lines)
        last_line = lines.pop()
        for i in range(diff):
            lines.append(fill("", len(last_line)))
        lines.append(last_line)
    return lines
