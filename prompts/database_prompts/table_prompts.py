from utils.databases import database
"""
Concerned with providing menu options to make changes to an individual users FineWise tracker(s)
"""


def choose_table_prompt(profile):
    while True:
        tracker = input("""Please enter the title of finance tracker you would like to use.
Enter the title here: """).lower().title()
        if database.check_table_name(profile, tracker):
            return tracker
        else:
            print(f"There is no finance tracker title: {tracker}. Try a different title.")


def display_all_trackers_prompt(profile):
    while True:
        all_data = input("""Please choose one of the following options:\n
-Enter 'a' to view ALL of the data in your finance tracker(s)
-OR-
-Enter 't' to view only the TITLES of each of your financial tracker(s)""").lower()
        if all_data == 'a':
            all_data = True
            break
        elif all_data == 't':
            all_data = False
            break
        else:
            print("\nThat was an invalid input. Let's try that again.\n")
    database.display_all_trackers(profile, all_data)


def add_table_prompt(profile):
    confirmation = ""
    while confirmation != 'y' and confirmation != 'n':
        confirmation = input("""Are you sure you wish to create a new finance tracker?
(Don't worry, this will NOT overwrite any pre-existing finance tracker(s))\n
-Enter 'y' for Yes
-or-
-Enter 'n' for No\n
Your choice: """).lower()
        if confirmation == 'n':
            print("Don't worry! Let's take it back a bit.")
            return
        elif confirmation == 'y':
            while True:
                tracker = input("""What would you like to name your new finance tracker?
Hint: Try to keep it simple, something short and to the point.\n
Title: """).lower().title()
                if not database.check_table_name(profile, tracker):
                    database.create_table(profile, tracker)
                    return tracker
                else:
                    print(f"""The {tracker} title has already been assigned to a finance tracker.
Try a different name instead.""")
        else:
            print("\nThat was an invalid input. Let's try that again.\n")


def delete_table_prompt(profile):
    while True:
        table_name = input("""Please enter the title of finance tracker you would like to delete.
        Enter the title here: """).lower().title()
        if database.check_table_name(profile, table_name):
            confirmation = ""
            while confirmation != 'y' and confirmation != 'n':
                confirmation = input(f"""Are you sure you want to delete your {table_name} finance tracker?
WARNING: This action cannot be undone.\n
-Enter 'y' to delete the {table_name} finance tracker
-or-
-Enter 'n' to keep the {table_name} finance tracker\n
Your choice: """).lower()
                if confirmation == 'y':
                    database.delete_table(profile, table_name)
                    break
                elif confirmation == 'n':
                    print(f"Don't worry, the {table_name} finance tracker will NOT be deleted")
                    break
                else:
                    print("\nThat was an invalid input. Let's try that again.\n")
            break
        else:
            print(f"There is no finance tracker title: {table_name}. Try a different title.")
