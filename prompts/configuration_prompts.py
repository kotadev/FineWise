from configurations import configure_dates, configure_metrics, configure_displays


def determine_order_prompt(considered):
    while True:
        choice = input(f"""Will this {considered} occur more than once in your finance tracker?\n
-Enter '1' if this {considered} is a ONE time deal.
-OR-
-Enter '2' if this {considered} will occur multiple times throughout your finance tracker\n
your choice: """)
        if choice == '1':
            start, frequency, stop = one_time_prompt()
            if start and frequency and stop:
                break
        elif choice == '2':
            start, frequency, stop = multiple_times_prompt(considered)
            if start and frequency and stop:
                break
        else:
            invalid()
    return start, frequency, stop


def one_time_prompt():
    print("What date will this occur?")
    start = set_date_prompt()
    if start:  # ['day', 'month', 'year']
        frequency = 'single once 1'
        stop = start
        return start, frequency, stop
    else:
        return False, False, False


def multiple_times_prompt(considered):
    while True:
        start, frequency = set_frequency_prompt(considered)
        if frequency and start:
            stop = set_stop_prompt(considered)
            if stop:
                return start, frequency, stop
        else:
            return False, False, False


def set_date_prompt():
    while True:
        while True:
            year_input = input(f"""Please enter the year you would like to use.
    Make sure to enter the year in `YYYY` format: """)
            if configure_dates.process_year_input(year_input):
                year_int = int(year_input)
                break
            else:
                invalid()
        while True:
            month_input = input(f"""Please enter the month of this date.
    Make sure to enter the month in `MM` format: """)
            if configure_dates.process_month_input(month_input):
                month_int = int(month_input)
                break
            else:
                invalid()
        while True:
            month_name = configure_dates.convert_month_to_string(month_input)
            day_input = input(f"""Please enter which day in {month_name} you would like to set as the date. 
    Make sure to enter the day in `DD` format: """)
            if configure_dates.process_day_input(day_input, month_int, year_int):
                day_int = int(day_input)
                break
            else:
                invalid()
            configure_displays.display_month(month_int, year_int)
        while True:
            confirmation = input(f"""You chose {month_int}/{day_int}/{year_int} as the date, is this correct?
-Enter '1' to CONFIRM
-Enter '2' to RESTART and choose a different start date
-OR-
-Enter '3' to go back to the previous menu\n
Your choice: """)
            if confirmation == '1':
                return f"{month_int} {day_int} {year_int}"
            elif confirmation == '2':
                print("Not a problem, let's go back to the beginning.\n")
                break
            elif confirmation == '3':
                return False
            else:
                invalid()


def set_frequency_prompt(considered):
    while True:
        metric = input(f"""How frequently does this {considered} occur?\n
-Enter '1' for daily
-Enter '2' for weekly
-Enter '3' for monthly
-Enter '4' for yearly
-OR-
-Enter '5' to set a custom frequency
-OR- 
Enter '6' to go back to the previous menu\n
Your choice: """).lower()
        if metric == '1' or metric == '2' or metric == '3' or metric == '4':
            print(f"When does will this {considered} begin to take affect?")
            start = set_date_prompt()
            if metric == '1':
                frequency = 'standard day 1'
            elif metric == '2':
                frequency = 'standard weekly 7'
            elif metric == '3':
                frequency = 'standard monthly tbd'
            else:
                frequency = 'standard yearly tbd'
            break
        elif metric == '5':
            start, frequency = set_custom_frequency_prompt(considered)
            if start and frequency:
                break
        elif metric == '6':
            start, frequency = False
            break
        else:
            invalid()
    return start, frequency


def set_custom_frequency_prompt(considered):
    while True:
        metric = input("""Which metric would you like your custom frequency to go by?\n
-Enter '1' for every 'x' day(s)
-Enter '2' for every 'x' week(s)
-Enter '3' for every 'x' month(s)
-Enter '4' for every 'x' year(s)\n
-Enter '5' for a specific day of the week every month
-OR-
-Enter '6' to go back to the previous menu\n
Your choice:""").lower()
        if metric == '1' or metric == '2' or metric == '3' or metric == '4':
            print(f"When does will this {considered} begin to take affect?")
            start = set_date_prompt()
            if metric == '1':
                num = input(f"""This {considered} happens every how many days?
Your Answer: """)
                metric = 'days'
            elif metric == '2':
                num = input(f"""This {considered} happens every how many weeks?
Your Answer: """)
                metric = 'weeks'
            elif metric == '3':
                num = input(f"""This {considered} happens every how many months?
Your Answer: """)
                metric = 'months'
            else:
                num = input(f"""This {considered} happens every how many years?
Your Answer: """)
                metric = 'years'
            frequency = f"custom {metric} {num}"
            break
        elif metric == '5':
            start, frequency = set_specific_frequency_prompt(considered)
            if start and frequency:
                break
        elif metric == '6':
            print("Not a problem. Let's take go back.\n")
            return False, False
        else:
            invalid()
    return start, frequency


def set_specific_frequency_prompt(considered):
    while True:
        metric = input(f"""Which day of the week does this {considered} occur?\n
-Enter '1' for Sunday
-Enter '2' for Monday
-Enter '3' for Tuesday
-Enter '4' for Wednesday
-Enter '5' for Thursday
-Enter '6' for Friday
-Enter '7' for Saturday\n
-OR-
-Enter '8' to go back to the previous menu\n
Your choice: """).lower()
        if metric == [day_num for day_num in ['1', '2', '3', '4', '5', '6', '7']]:
            if metric == '1':
                metric = 'Sunday'
            elif metric == '2':
                metric = 'Monday'
            elif metric == '3':
                metric = 'Tuesday'
            elif metric == '4':
                metric = 'Wednesday'
            elif metric == '5':
                metric = 'Thursday'
            elif metric == '6':
                metric = 'Friday'
            else:
                metric = 'Saturday'
            num = configure_metrics.set_specific_frequency(considered, metric)
            if num:
                frequency = f"custom {metric} {num}"
                print(f"When does will this {considered} begin to take affect?")
                start = set_date_prompt()
                if start:
                    break
        if metric == '8':
            print("Not a problem. Let's take go back.\n")
            return False, False
        else:
            if metric:
                frequency = configure_metrics.set_specific_frequency(considered, metric)
                print(f"When does will this {considered} begin to take affect?")
                start = set_date_prompt()
                break
            else:
                invalid()
    return start, frequency


def set_stop_prompt(considered):
    while True:
        choice = input(f"""Is this {considered} temporary, or will it occur indefinitely?\n
-Enter '1' to apply the {considered} INDEFINITELY (without an end date)
-OR-
-Enter '2' to set a date for when this {considered} will STOP.\n
Your choice: """)
        if choice == '1':
            return '0 0 0'
        elif choice == '2':
            stop = set_date_prompt()
            return stop
        else:
            invalid()


# def simulate_data_prompt(profile, table_name):
#    pass


def invalid():
    print("\nThat was an invalid input. Let's try that again.\n")
