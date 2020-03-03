"""
Concerned with providing finished data within a FineWise tracker,
which includes frequencies, start dates, and stop dates 
"""


def set_metric_values(metric, choice):
    metric_values = {
        'su': 'Sunday',
        'm': 'Monday',
        't': 'Tuesday',
        'w': 'Wednesday',
        'th': 'Thursday',
        'f': 'Friday',
        'sa': 'Saturday'
    }


def check_value(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def set_custom_frequency(considered, metric):
    while True:
        x = input(f"This {considered} happens every how many {metric}?")
        try:
            int(x)
            break
        except ValueError:
            invalid()

    return f"custom {metric} {x}"


def set_specific_frequency(considered, metric):
    print(f"This {considered} happens on which {metric} of every month?")
    while True:
        try:
            num = int(input(f"""-Enter 1 for the first
-Enter 2 for the second
-Enter 3 for the third
-Enter 4 for the fourth
-Enter 5 to specify the last {metric} of every month
-OR-
-Enter 6 to go back to the previous menu\n
Your choice:"""))
            if 0 < int(num) < 6:
                return num
            elif num == '6':
                return False
            else:
                invalid()
        except ValueError:
            invalid()


def invalid():
    print("\nThat was an invalid input. Let's try that again.\n")
