from prompts.startup_prompts import main_prompts
from prompts.database_prompts import data_prompts
from prompts import calendar_prompts


def setup_menu():
    print("Hello, and welcome to FineWise. The easy to use easy and to understand financial tracker and calculator.\n")
    while True:
        choice = input("""Are you ready to start your FineWise journey to financial management?\n
-Enter '1' to begin
-OR-
-Enter '2' to close the FineWise app.\n
Your choice: """)
        if choice == '1':
            return main_prompts.create_admin_prompt()
        elif choice == '2':
            print("See you later!")
            raise SystemExit
        else:
            invalid()


def main_menu():
    print("Hello, and welcome to FineWise. The easy to use easy to understand financial tracker and calculator.\n")
    while True:
        choice = input("""What is it that you would like to do today?\n
-Enter '1' to sign-in
-Enter '2' to create a new account
-Enter '3' to delete an existing account
-Enter '4' to permanently reset the FineWise app
-OR-
-Enter '0' to close the FineWise app.\n
Your choice: """)
        if choice == '1':
            return main_prompts.sign_in_prompt()
        elif choice == '2':
            return main_prompts.create_profile_prompt()
        elif choice == '3':
            main_prompts.delete_profile_prompt()
        elif choice == '4':
            reset = main_prompts.hard_reset_prompt()
            if reset:
                raise SystemExit
        elif choice == '0':
            raise SystemExit
        else:
            invalid()


def tracker_menu(profile):
    print(f"\nHello {profile}!\n")
    while True:
        choice = input("""What would you like to do?\n
You can:
-Enter '1' to continue to your finance tracker
-Enter '2' to start a new finance tracker
-Enter '3' to go back to the previous menu options
-OR-
-Enter '0' to exit FineWise\n
Your choice: """)
        if choice == '1':
            return True
        elif choice == '2':
            main_prompts.reset_tracker_prompt(profile)
        elif choice == '3':
            return False
        elif choice == '0':
            raise SystemExit
        else:
            invalid()


def data_menu(profile):
    while True:
        choice = input(f"""What would you like to do with your finance tracker?\n
You can:
-Enter '1' to view your financial tracker calendar
-Enter '2' to view your finances in your financial tracker
-Enter '3' to add new finances to your financial tracker
-Enter '4' to delete finances from your financial tracker
-Enter '5' to go back to the previous menu options
-OR-
-Enter '0' to quit the FineWise application\n
Your choice: """)
        if choice == '1':
            return True
        elif choice == '2':
            data_prompts.view_data_prompt(profile)
        elif choice == '3':
            data_prompts.add_data_prompt(profile)
        elif choice == '4':
            data_prompts.delete_data_prompt(profile)
        elif choice == '5':
            return False
        elif choice == '0':
            raise SystemExit
        else:
            invalid()


def calendar_menu(day, month, year, profile):   # Remember to convert the string '02-18-2020' to month= 2, day= 18, year= 2020
    while True:                       # for Date strings   DO IN APP.PY!!!!  JUST NEED CURRENT DATE TO START
        choice = input("""-Enter '1' to view your tracker year by year
-Enter '2' to view your tracker month by month
-Enter '3' to view your tracker week by week
-Enter '4' to view your tracker day by day
-Enter '5' to view your tracker at a specific date
-Enter '6' to go back to the previous menu options
-OR-
-Enter '0' to quit the FineWise application\n
Your choice: """)
        if choice == '1':
            calendar_prompts.yearly_view_prompt(year, profile)
        elif choice == '2':
            calendar_prompts.monthly_view_prompt(month, year, profile)
        elif choice == '3':
            calendar_prompts.weekly_view_prompt(day, month, year, profile)
        elif choice == '4':
            calendar_prompts.daily_view_prompt(day, month, year, profile)
        elif choice == '5':
            calendar_prompts.date_view_prompt(profile)
        elif choice == '6':
            return False
        elif choice == '0':
            raise SystemExit
        else:
            invalid()


def invalid():
    print("\nThat was an invalid input. Let's try that again.\n")
