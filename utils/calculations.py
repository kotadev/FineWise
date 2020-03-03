from utils.databases import finances_tools
from utils import data_tools


def calculate(view, day_int, month_int, year_int, profile):
    viewable_finances = [0, 0, 0]
    tracker_data = finances_tools.get_finance_data(profile)
    if view == 'year':
        view_details, view_info = calculate_year(year_int, tracker_data, viewable_finances)
    elif view == 'month':
        view_details, view_info = calculate_month(month_int, year_int, tracker_data, viewable_finances)
    elif view == 'week':
        view_details, view_info = calculate_week(day_int, month_int, year_int, tracker_data, viewable_finances)
    else:
        view_details, view_info = calculate_day(day_int, month_int, year_int, tracker_data, viewable_finances)
    # current_data, current_details = calculate_current(day, month, year, tracker_data, viewable_finances)
    print(view_details)
    print(view_info)
    """print(current_data)
    print(current_details)"""


def results(beginning, end, tracker_data, finance_records, heading):
    income, expense, savings, leftover, information = finance_data(beginning, end, tracker_data, finance_records)
    details = f"""Financial Levels {heading}:
            Income: {income} | Expenses: {expense} | Savings: {savings} | Spendable: {leftover}"""
    info = f"""Here's all of your financial data {heading}:
            {''.join(information)}"""
    return details, info


def finance_data(beginning, end, tracker_data, finance_records):

    applicable_data = data_tools.get_applicable_data(beginning, tracker_data, end)

    finances, view_data = data_tools.assign_data(applicable_data, tracker_data, finance_records)
    income = finances[0]
    expense = finances[1]
    savings = finances[2]
    leftover = income - (expense + savings)
    information = [data_tools.print_data(info) for info in view_data]
    return income, expense, savings, leftover, information


def calculate_current(day, month, year, tracker_data, finance_records):
    heading = 'to Date'
    end = [day, month, year]
    beginning = [0, 0, 0]
    details, info = results(beginning, end, tracker_data, finance_records, heading)
    return details, info


def calculate_year(year_int, tracker_data, finance_records):
    heading = f'for {year_int}'
    beginning = [1, 1, year_int]
    end = [1, 1, (year_int + 1)]
    details, info = results(beginning, end, tracker_data, finance_records, heading)
    return details, info


def calculate_month(month, year, tracker_data, finance_records):
    heading = f'for {month}'
    beginning = [1, month, year]
    if month + 1 == 13:
        end = [1, 1, (year + 1)]
    else:
        end = [1, (month + 1), year]
    return results(beginning, end, tracker_data, finance_records, heading)


def calculate_week(day, month, year, tracker_data, finance_records):
    heading, beginning, end = data_tools.calibrate_week_info(day, month, year)
    return results(beginning, end, tracker_data, finance_records, heading)


def calculate_day(day, month, year, tracker_data, finance_records):
    heading = f'for {[month, day, year]}'
    beginning = [1, month, year]
    end = beginning
    return results(beginning, end, tracker_data, finance_records, heading)
