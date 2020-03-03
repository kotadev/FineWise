from utils.databases import finances_tools
from prompts import configuration_prompts
"""
Concerned with providing menu options to add, edit, and view data within a FineWise tracker,
as well as simulate the application of any of these menu options.
"""


def view_data_prompt(profile):
    while True:
        choice = input(f"""Please choose one of the following options:\n
-Enter '1' to view ALL of the data in your finance tracker
-OR-
-Enter '2' to go back to the previous menu\n
Your choice: """)
        if choice == '1':
            finances_tools.view_data(profile)
            return
        elif choice == '2':
            return
        else:
            print("\nThat was an invalid input. Let's try that again.\n")


def add_data_prompt(profile):
    category = input("""What category would this financial data fall under?
For example, you could enter 'Auto', 'Housing', 'Paycheck', 'Utilities', or anything else!\n
Name of category: """).title()
    while True:
        title = input("Enter the name of this new financial data: ").title()
        if not finances_tools.check_for_title(profile, title):
            break
        else:
            print('That name is already taken by another piece of financial data. Try a different name.\n')
    while True:
        considered = input("""-Enter '1' if this is considered income
-Enter '2' if this is considered an expense
-OR-
-Enter '3' if this is considered a savings contribution\n
Your response: """).lower()
        if considered == '1':
            considered = 'income'
            break
        elif considered == '2':
            considered = 'expense'
            break
        elif considered == '3':
            considered = 'savings contribution'
            break
        else:
            print("\nThat was an invalid input. Let's try that again.\n")
    while True:
        amount = input("Please enter the dollar amount of this data as `###.##`: ")
        try:
            amount = float(amount)
            break
        except ValueError:
            print("\nThat was an invalid input. Let's try that again.\n")
    start, frequency, stop = configuration_prompts.determine_order_prompt(considered)
    finances_tools.add_data(profile, title, category, considered, amount, start, frequency, stop)


def delete_data_prompt(profile):
    while True:
        confirmation = input(f"""Are you sure you want to delete a piece of data from your finance tracker?
-Enter '1' for YES
-OR-
-Enter '2' for NO\n
Your choice: """).lower()
        if confirmation == '1':
            break
        elif confirmation == '2':
            print("Don't worry. Let's go back to the previous menu...")
            return
        else:
            print("\nThat was an invalid input. Let's try that again.\n")
    while True:
        title = input("Enter the name of the data you would like to delete: ")
        if finances_tools.check_for_title(profile, title):
            break
        else:
            print(f"There is no data name: {title} in your finance tracker at this time.")
            return
    while True:
        confirmation = input(f"""Are you sure you want to delete {title} from your finance tracker?
WARNING: This action cannot be undone!\n
-Enter '1' for YES
-OR-
-Enter '2' for NO\n
Your choice: """).lower()
        if confirmation == '1':
            break
        elif confirmation == '2':
            print("Don't worry. Let's go back to the previous menu...")
            return
        else:
            print("\nThat was an invalid input. Let's try that again.\n")
    finances_tools.delete_data(profile, title)
