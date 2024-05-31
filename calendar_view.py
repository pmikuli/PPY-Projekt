from datetime import datetime
from datetime import timedelta
from typing import List


def generate_week_lines(calendar, date: datetime):
    temp = []
    max_len = 0

    week_start = date - timedelta(days=date.weekday())
    for i in range(7):
        lines = calendar.generate_day_lines(week_start + timedelta(days=i), 41)
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


def generate_day_lines(calendar, date: datetime, width=80) -> List[str]:
    result = []

    lines = []
    i = 1

    for event in calendar.events:
        if are_days_equal(event.date_from, date) or are_days_equal(event.date_to, date):
            if are_days_equal(event.date_from, event.date_to):
                line = (event.date_from.strftime("%H:%M") + "-"
                        + event.date_to.strftime("%H:%M") + " " + event.name)
            else:
                line = (event.date_from.strftime(calendar.date_format + " %H:%M") + " - "
                        + event.date_to.strftime(calendar.date_format + " %H:%M") + " " + event.name)

            if len(line) + 4 > width:
                # save space for "|" at the beginning and end + space
                chunk_size = width - len(str(i)) - 6
                start = chunk_size + len(str(i))
                lines.append(fill(line[0:start], width))  # doesn't require space
                chunks = [line[i:i + chunk_size] for i in range(start, len(line), chunk_size)]
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

    day_of_the_week_line = date.strftime("%A")
    result.append(center(day_of_the_week_line, width))

    date_line = date.strftime(calendar.date_format)
    w = width
    if are_days_equal(date, datetime.now()):
        date_line = "\033[95m" + date_line + "\033[0m"
        # The color characters are invisible, but
        # they still count to len(date_line) which is used
        # center the text.
        # Thus, we need to increase width by number of additional characters
        w = width + 9
    result.append(center(date_line, w))

    result.append(separator_line)
    for line in lines:
        result.append(line)
    result.append(separator_line)

    return result

def generate_month(calendar, date: datetime) -> List[str]:
    if date.day != 1:
        diff = date.day - 1
        date = date - timedelta(days=diff)
    header_str = date.strftime("%B %Y")
    month = date.month
    lines = []
    while month == date.month:
        line = ""

        for i in range(7):
            if date.weekday() == i:
                date_str = ""
                if are_days_equal(date, datetime.now()):
                    date_str = "\033[95m" + str(date.day) + "\033[0m"
                else:
                    date_str = str(date.day)
                if date.day < 10:
                    line += ("  " + date_str + " ")
                else:
                    line += (" " + date_str + " ")
                date = date + timedelta(days=1)
            else:
                line += "    "
        lines.append("| " + line + " |")
    separator = ""
    for i in range(len(lines[0])):
        separator += "-"

    result = [separator, center(header_str, len(lines[0])), separator]

    result.extend(lines)
    result.append(separator)

    return result


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


def are_days_equal(date1, date2):
    return (date1.day == date2.day
            and date1.month == date2.month
            and date1.year == date2.year)
