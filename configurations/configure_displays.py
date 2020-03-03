import calendar
from datetime import date


def current_calendar():
    today = date.today()
    year = int(today.strftime("%Y"))
    display_calendar(year)
    return year


def display_calendar(year_int):
    print(f"Here is a monthly calendar for the current {year_int} year:")
    for month in range(1, 13):
        calendar_view = calendar.TextCalendar(calendar.SUNDAY)
        user_view = calendar_view.formatmonth(year_int, month)
        print(user_view)


def display_month(month_int, year_int):
    calendar_view = calendar.TextCalendar(calendar.SUNDAY)
    user_view = calendar_view.formatmonth(year_int, month_int)
    print(user_view)


def display_week(week_dates, year_info):
    days = calendar.weekheader(3).split()
    single_space = " "
    double_space = "  "
    dates = []
    for num in week_dates:
        if num < 10:
            dates.append(f"{num}{double_space}")
        else:
            dates.append(f"{num}{single_space}")

    user_view = f"""{year_info}
| {days[0]}| {days[1]}| {days[2]}| {days[3]}| {days[4]}| {days[5]}| {days[6]}|
| {dates[0]}| {dates[1]}| {dates[2]}| {dates[3]}| {dates[4]}| {dates[5]}| {dates[6]}|"""
    print(user_view)


def display_day(day_name, day_int, month_int, year_year):
    print(f"""{day_name}, {month_int} {day_int}, {year_year}""")

