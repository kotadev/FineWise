from utils.databases import database, profile_tools, finances_tools
"""
Concerned with providing menu options when the system detects that a `profiles.db` file
exists within the application upon initialization.
"""


def create_admin_prompt():
    status = 'admin'
    username = input("Please enter your desired username: ")
    while True:
        pin_entry = input("Please enter a 7-digit PIN that you will remember to use as your password: ")
        if len(pin_entry) == 7:
            try:
                pin = int(pin_entry)
                break
            except ValueError:
                print("\nThat was an invalid input. Let's try that again.\n")
        else:
            print("Your PIN must be EXACTLY 7-digits long.\n")
    database.create_profiles()
    database.create_table()
    return profile_tools.add_profile(username, status, pin)


def sign_in_prompt():
    attempts = 0
    while attempts < 3:
        username = input("Please enter your username: ")
        pin = input("Please enter your PIN: ")
        if profile_tools.sign_in(username, pin):
            return username
        elif attempts < 3:
            attempts += 1
            print(f"That was incorrect. {3 - attempts} remaining.")
    print("Too many attempts. Shutting down.")
    raise SystemExit


def create_profile_prompt():
    status = 'user'
    while True:
        username = input("Please enter your desired username: ")
        if not profile_tools.check_for_username(username):
            break
        else:
            print("Sorry, that username has already been taken. Please choose a different username.\n")
    while True:
        pin_entry = input("Please enter a 4-digit PIN that you will remember to use as your password: ")
        if len(pin_entry) == 4:
            try:
                pin = int(pin_entry)
                break
            except ValueError:
                print("\nThat was an invalid input. Let's try that again.\n")
        else:
            print("Your PIN must be EXACTLY 4-digits long.\n")
    profile_tools.add_profile(username, status, pin)


def delete_profile_prompt():
    attempts = 0
    while attempts < 3:
        username = input("Please enter the name of the username you wish to delete: ")
        pin = input("Please enter your PIN: ")
        if profile_tools.sign_in(username, pin):
            if profile_tools.check_admin(username):
                print("Sorry. You must choose a new app admin in before deleting your account")
                return
            while True:
                confirmation = input(f"""Are you sure you want to delete {username}'s account forever?
WARNING: This cannot be undone and all of {username}'s finance trackers will be deleted forever as well!\n
-Enter 'y' for YES
-or-
-Enter 'n' for NO\n
Your choice: """).lower()
                if confirmation == 'y':
                    print(f"Deleting {username}'s account forever...")
                    profile_tools.delete_profile(username)
                    print(f"Done!")

                    return
        else:
            attempts += 1
            if attempts < 3:
                print(f"That was incorrect. {3 - attempts} remaining.")
    print("Too many attempts. Shutting down.")
    raise SystemExit


def hard_reset_prompt():
    confirmation = ""
    while confirmation != 'y' and confirmation != 'n':
        confirmation = input("""Are you sure you want to start a new experience?
        Doing so will DELETE ALL currently existing profiles and finance trackers on your FineWise app!\n
        -Enter '1' for YES
        -or-
        -Enter '2' for NO\n
        Your choice: """).lower()
        if confirmation == '1':
            profile_tools.hard_reset()
            return True
        elif confirmation == '2':
            print("Returning to main menu...")
            return False
        else:
            print("\nThat was an invalid input. Let's try that again.\n")


def reset_tracker_prompt(profile):
    confirmation = ""
    while confirmation != 'y' and confirmation != 'n':
        confirmation = input("""Are you sure you want to start a new finance tracker?
            Doing so will DELETE ALL currently existing data in your finance tracker!\n
            -Enter '1' for YES
            -or-
            -Enter '2' for NO\n
            Your choice: """).lower()
        if confirmation == '1':
            finances_tools.reset_tracker(profile)
            return True
        elif confirmation == '2':
            print("Returning to main menu...")
            return False
        else:
            print("\nThat was an invalid input. Let's try that again.\n")