import calendar
from datetime import date

month_names = {
    '01': 'January', '1': 'January',
    '02': 'February', '2': 'February',
    '03': 'March', '3': 'March',
    '04': 'April', '4': 'April',
    '05': 'May', '5': 'May',
    '06': 'June', '6': 'June',
    '07': 'July', '7': 'July',
    '08': 'August', '8': 'August',
    '09': 'September', '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}


def get_current_year():
    today = date.today()
    year = today.strftime("%Y")
    return int(year)


def get_current_month():
    today = date.today()
    month = today.strftime("%m")
    return int(month)


def get_current_day():
    today = date.today()
    day = today.strftime("%d")
    return int(day)


def get_week(day_int, month_int, year_int):
    c = calendar.Calendar(firstweekday=6)
    weeks = c.monthdayscalendar(year_int, month_int)
    for week in range(len(weeks)):
        for weekday in weeks[week]:
            if day_int == weekday:
                return week


def process_year_input(year_input):
    try:
        int(year_input)
        if len(year_input) == 4:
            return True
        else:
            return False
    except ValueError:
        return False


def process_month_input(month_input):
    try:
        if 0 < int(month_input) < 13:
            return True
        else:
            return False
    except KeyError:
        return False


def process_day_input(day_input, month_int, year_int):
    reference = calendar.TextCalendar(calendar.SUNDAY)
    days_in_month = [int(num) for num in reference.itermonthdays(year_int, month_int) if int(num) > 0]
    for num in reference.itermonthdays(year_int, month_int):
        if num > 0:
            days_in_month.append(num)
    try:
        if int(day_input) in days_in_month:
            return True
        else:
            return False
    except ValueError:
        return False


def last_week_in_month(year_int, month_int):
    c = calendar.Calendar(firstweekday=6)
    weeks = c.monthdayscalendar(year_int, month_int)
    return len(weeks) - 1


def last_day_in_month(month_int, year_int):
    c = calendar.TextCalendar(calendar.SUNDAY)
    days_in_month = [int(date_num) for date_num in c.itermonthdays(year_int, month_int) if int(date_num) > 0]
    return days_in_month[-1]


def combine_weeks(week, year_int, month_int, display):
    other_week, other_month, other_year = get_other_week_info(week, month_int, year_int)
    if week == 0:
        other_week_dates = get_week_dates(other_week, other_month, other_year)
        week_dates = get_week_dates(week, month_int, year_int)
        dates = other_week_dates + week_dates
    else:
        week_dates = get_week_dates(week, month_int, year_int)
        other_week_dates = get_week_dates(other_week, other_month, other_year)
        dates = week_dates + other_week_dates
    year_info = get_year_info(month_int, year_int, other_month, other_year, display)
    return dates, year_info


def get_year_info(month_int, year_int, other_month, other_year, display):  # Come back to!!!!
    if display:
        month_name = month_names[str(month_int)]
        other_month = month_names[str(other_month)]
        if year_int < other_year:
            year_info = f"{month_name} {year_int} - {other_month} {other_year}"
        elif other_year < year_int:
            year_info = f"{other_month} {other_year} - {month_name} {year_int}"
        else:
            year_info = f"{month_name} {year_int}"
    else:
        if year_int < other_year:
            year_info = f"1 {month_int} {year_int} {other_month} {other_year}"
        elif other_year < year_int:
            year_info = f"2 {other_month} {other_year} {month_int} {year_int}"
        else:
            year_info = f"{month_int} {year_int}"

    return year_info


def get_other_week_info(week, month_int, year_int):
    if week == 0:
        if month_int == 1:
            other_month = 12
            other_year = year_int - 1
        else:
            other_month = month_int - 1
            other_year = year_int
        other_week = last_week_in_month(other_year, other_month)
    else:
        if month_int == 12:
            other_month = 1
            other_year = year_int + 1
        else:
            other_month = month_int + 1
            other_year = year_int
        other_week = 0
    return other_week, other_month, other_year


def get_week_dates(week, month_int, year_int):
    c = calendar.Calendar(firstweekday=6)
    calendar_view = c.monthdayscalendar(year_int, month_int)
    week_dates = calendar_view[week]
    dates = [int(num) for num in week_dates if int(num) != 0]
    month_name = month_names[str(month_int)]
    year_info = f"{month_name} {year_int}"
    return dates, year_info


def process_day_change(choice, day_changes, day_int, month_int, year_int, last_date):
    for count in range(day_changes):
        if choice == '1':
            day_int -= 1
            if day_int == 0:
                month_int -= 1
                if month_int == 0:
                    month_int = 12
                    year_int -= 1
                day_int = last_date
            return day_int, month_int, year_int
        elif choice == '2':
            day_int += 1
            if day_int > last_date:
                day_int = 1
                month_int += 1
                if month_int == 12:
                    month_int = 1
                    year_int += 1
            return day_int, month_int, year_int


def get_day_name(day_int, month_int, year_int):
    day_str = str(day_int)
    weeks = range(last_week_in_month(year_int, month_int))
    c = calendar.monthcalendar(year_int, month_int)
    for week in weeks:
        week = c[week]
        if day_str == week[calendar.SUNDAY]:
            return 'Sunday'
        elif day_str == week[calendar.MONDAY]:
            return 'Monday'
        elif day_str == week[calendar.TUESDAY]:
            return 'Tuesday'
        elif day_str == week[calendar.WEDNESDAY]:
            return 'Wednesday'
        elif day_str == week[calendar.THURSDAY]:
            return 'Thursday'
        elif day_str == week[calendar.FRIDAY]:
            return 'Friday'
        elif day_str == week[calendar.SATURDAY]:
            return 'Saturday'


def convert_month_to_string(month_input):
    return month_names[str(month_input)]


def invalid():
    print("\nThat was an invalid input. Let's try that again.\n")
