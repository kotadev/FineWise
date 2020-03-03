from configurations import configure_dates, configure_displays
from utils.calculations import calculate


def get_choice_prompt(view):
    return input(f"""-Enter '1' to view the previous {view}
-Enter '2' to view the next {view}
-Enter '3' to reset the {view} to the current {view}
-Enter '4' to go back to the previous menu options
-OR-
-Enter '0' to quit the FineWise application\n
Your choice: """)


def yearly_view_prompt(year, profile):
    view = 'year'
    day_int = 1
    month_int = 1
    year_int = int(year)
    while True:
        configure_displays.display_calendar(year_int)
        calculate(view, day_int, month_int, year_int, profile)
        choice = get_choice_prompt(view)
        if choice == '1':
            year_int -= 1
        elif choice == '2':
            year_int += 1
        elif choice == '3':
            year_int = configure_dates.get_current_year()
        elif choice == '4':
            return
        elif choice == '0':
            raise SystemExit
        else:
            invalid()


def monthly_view_prompt(month, year, profile):
    view = 'month'
    day_int = 1
    month_int = int(month)
    year_int = int(year)
    while True:
        configure_displays.display_month(year_int, month_int)
        # calculate(view, day, month, year, profile)
        choice = get_choice_prompt(view)
        if choice == '1':
            month_int -= 1
            if month_int == 0:
                month_int = 12
                year_int -= 1
        elif choice == '2':
            month_int += 1
            if month_int == 13:
                month_int = 1
                year_int += 1
        elif choice == '3':
            month_int = configure_dates.get_current_month()
            year_int = configure_dates.get_current_year()
        elif choice == '4':
            return
        else:
            invalid()


def weekly_view_prompt(day, month, year, profile):
    day_changes = 7
    view = 'week'
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)
    while True:
        week = configure_dates.get_week(day_int, month_int, year_int)
        last_week = configure_dates.last_week_in_month(year_int, month_int)
        if week == 0 or week == last_week:
            week_dates, year_info = configure_dates.combine_weeks(week, month_int, year_int, True)
        else:
            week_dates, year_info = configure_dates.get_week_dates(week, month_int, year_int)
        configure_displays.display_week(week_dates, year_info)
        # calculate(view, day, month, year_int, profile)
        last_date = configure_dates.last_day_in_month(year_int, month_int)
        choice = get_choice_prompt(view)
        if choice == '1' or choice == '2':
            day_int, month_int, year_int = configure_dates.process_day_change(choice, day_changes, day_int, month_int, year_int, last_date)
        elif choice == '3':
            day_int = configure_dates.get_current_day()
            month_int = configure_dates.get_current_month()
            year_int = configure_dates.get_current_year()
        elif choice == '4':
            return
        elif choice == '0':
            pass


def daily_view_prompt(day, month, year, profile):
    day_changes = 1
    view = 'day'
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)
    while True:
        day_name = configure_dates.get_day_name(day_int, month_int, year_int)
        configure_displays.display_day(day_name, day_int, month_int, year_int)
        # calculate(view, day, month, year, profile)
        last_date = configure_dates.last_day_in_month(year_int, month_int)
        choice = get_choice_prompt(view)
        if choice == '1' or choice == '2':
            day, month, year_int = configure_dates.process_day_change(choice, day_changes, day_int, month_int, year_int, last_date)
        elif choice == '3':
            day_int = configure_dates.get_current_day()
            month_int = configure_dates.get_current_month()
            year_int = configure_dates.get_current_year()
        elif choice == '4':
            return
        elif choice == '0':
            raise SystemExit
        else:
            invalid()


def date_view_prompt(profile):
    view = "single"
    while True:
        year_input = input(f"""Please enter the year of the date you are looking into.
Make sure to enter the year in `YYYY` format: """)
        if configure_dates.process_year_input(year_input):
            year_int = int(year_input)
            break
        else:
            invalid()
    while True:
        month_input = input(f"""Please enter the month of the date you are looking into.
Make sure to enter the year in `MM` format: """)
        if configure_dates.process_month_input(month_input):
            month_int = int(month_input)
            break
        else:
            invalid()
    while True:
        day_input = input(f"""Please enter which day in {month_int} you would like to set as the date. 
Make sure to enter the day in `DD` format: """)
        if configure_dates.process_day_input(day_input, month_int, year_int):
            day_int = int(day_input)
            break
        else:
            invalid()
    day_name = configure_dates.get_day_name(day_int, month_int, year_int)
    configure_displays.display_day(day_name, day_int, month_int, year_int)
    # calculate(view, day, month, year, profile)


def invalid():
    print("\nThat was an invalid input. Let's try that again.\n")
