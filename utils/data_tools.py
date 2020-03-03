import calendar
from configurations import configure_dates


def get_applicable_data(beginning, tracker_data, end):
    applicable_data = []
    for info in tracker_data:
        start_date, frequency_info, stop_date = pull_data(info)
        active_dates = {'name': info['name'], 'occurrences': get_occurrences(beginning, start_date, stop_date, frequency_info, end)}
        applicable_data.append(active_dates)

    return applicable_data


def pull_data(info):
    start_date = [int(info['start'].split()[1]), int(info['start'].split()[0]), int(info['start'].split()[2])]
    frequency_info = info['frequency'].split()
    stop_date = [int(info['stop'].split()[1]), int(info['stop'].split()[0]), int(info['stop'].split()[2])]
    return start_date, frequency_info, stop_date


def get_occurrences(beginning, start_date, stop_date, frequency_info, end):

    day_num, month_num, year_num = [num for num in beginning]
    current_date = [day_num, month_num, year_num]
    active_day = start_date[1]
    active_month = start_date[0]
    active_year = start_date[2]
    active_date = [active_day, active_month, active_year]
    occurrences = 0
    last_date = configure_dates.last_day_in_month(month_num, year_num)
    if calendar.isleap(year_num):
        days_in_year = 366
    else:
        days_in_year = 365
    metrics = [
        ['single', 'once', 1],
        ['standard', 'daily', 1],
        ['standard', 'weekly', 7],
        ['standard', 'monthly', last_date],
        ['standard', 'yearly', days_in_year]
    ]

    if frequency_info[0] == 'single':
        occurrences = 1

    elif frequency_info[0] == 'standard':  # If a standard frequency
        for metric in metrics:
            if frequency_info[1] == metric[1]:
                while current_date != end:
                    if frequency_info[1] == 'monthly':
                        interval = last_date
                    elif frequency_info[1] == 'yearly':
                        interval = days_in_year
                    else:
                        interval = metric[2]
                    if active(year_num, month_num, day_num, start_date, stop_date):
                        print("active")
                        if current_date == active_date:
                            print(active_date)
                            print(current_date)
                            occurrences += 1
                            for days in range(interval):
                                active_day, active_month, active_year, last_date, days_in_year = increment_day(active_day, active_month, active_year)
                            active_date = [active_day, active_month, active_year]
                    day_num, month_num, year_num, last_date, days_in_year = increment_day(day_num, month_num, year_num)
                    current_date = [day_num, month_num, year_num]
    return occurrences


def active(active_year, active_month, active_day, start_date, stop_date):
    if active_year > start_date[2] or (
            active_year == start_date[2] and active_month > start_date[1] or (active_year == start_date[2] and active_month == start_date[1] and active_day >= start_date[0])):
        if stop_date[2] == 0 or (active_year < stop_date[2]) or (
                active_year == stop_date[2] and active_month < stop_date[1] or (active_year == stop_date[2] and active_month == stop_date[1] and active_day < stop_date[0])):
            return True
    return False


def increment_day(day, month, year):
    last_date = configure_dates.last_day_in_month(month, year)
    day += 1
    if day > last_date:
        day = 1
        month += 1
        if month == 12:
            month = 1
            year += 1
    last_date = configure_dates.last_day_in_month(month, year)
    if calendar.isleap(year):
        days_in_year = 366
    else:
        days_in_year = 365
    return day, month, year, last_date, days_in_year


def assign_data(applicable_data, tracker_data, finance_records):
    finances = finance_records
    print(finances)
    view_data = []
    for info in tracker_data:
        for applicable in applicable_data:
            if info['name'] == applicable['name']:
                view_data.append(info)
                print(info['amount'])
                print(info['considered'])
                print(applicable['occurrences'])
                for occurrence in range(applicable['occurrences']):
                    if info['considered'] == 'income':
                        finances[0] += info['amount']
                        print(finances[0])
                    elif info['considered'] == 'expense':
                        finances[1] += info['amount']
                    else:
                        finances[2] += info['amount']

    view_data = sort_by_date(view_data)

    return finances, view_data


def sort_by_date(view_data):
    def sort_date(val):
        val_str = val.get('start').split()
        return val_str[2], val_str[0], val_str[1]
    view_data.sort(key=sort_date)
    for data in view_data:
        data_str = data.get('start').split()
        y, m, d = data_str[2], data_str[0], data_str[1]
        data['start'] = f"{m} {d} {y}"
    return view_data


def calibrate_week_info(day, month, year):
    week_dates, year_info = get_week_details(day, month, year)
    year_info = [int(num) for num in year_info.split()]
    if len(year_info) == 5:
        if year_info[0] == 1:
            month = year_info[1]
            year = year_info[2]
            end_month = year_info[3]
            end_year = year_info[4]
        else:
            month = year_info[3]
            year = year_info[4]
            end_month = year_info[1]
            end_year = year_info[2]
        end_day = week_dates[1]
        heading = f'this week in {month} {year} - {month} {year}'
    else:
        month = year_info[0]
        year = year_info[1]
        if is_last(week_dates[-1], year, month):
            end_day, end_month, end_year, _ = increment_day(week_dates[-1], month, year)
        else:
            end_day, end_month, end_year = week_dates[-1], month, year
        heading = f'this week in {month}, {year}'
    beginning = [week_dates[1], month, year]
    end = [end_day, end_month, end_year]
    return heading, beginning, end


def get_week_details(day, month, year):
    week = configure_dates.get_week(day, month, year)
    last_week = configure_dates.last_week_in_month(year, month)
    if week == 0 or week == last_week:
        return configure_dates.combine_weeks(week, month, year, False)
    else:
        return configure_dates.get_week_dates(week, month, year), f'{month} {year}'


def is_last(date, month, year):
    if date == configure_dates.last_day_in_month(year, month):
        return True
    else:
        return False


def print_data(data):
    return f"""Name: {data['name']} | Category: {data['category']} |
    Considered: {data['considered']} | Amount: {data['amount']} | Frequency: {data['frequency']} |
    Start Date: {data['start']} | Stop Date: {data['stop']} |\n\n"""


"""
Frequency can be:
1 day
-----------
1 daily
1 weekly
1 monthly
1 yearly
-----------
x days
x weeks
x months
x years
-----------
every 1st, 2nd, 3rd, 4th, or last, day_name of the month
"""
"""
start can = 'day month year'
stop can = start, 'indefinite', 'day month year'
"""