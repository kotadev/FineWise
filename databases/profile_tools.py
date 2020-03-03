from utils.databases.database_connection import DatabaseConnection
from utils.databases import database


def add_profile(username, status, pin):
    values = (username, status, pin,)
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO profiles VALUES(?, ?, ?)', values)

    return username


def sign_in(username, pin):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM profiles')
        profiles = [{'username': row[0], 'status': row[1], 'pin': row[2]} for row in cursor.fetchall()]

    for profile in profiles:
        if profile['username'] == username and profile['pin'] == int(pin):
            return True

    return False


def check_for_username(profile):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT username FROM profiles WHERE username = ?', (profile,))
        data = cursor.fetchone()

    if data is None:
        return False
    else:
        return True


def check_pin_pattern(status):
    while True:
        pin_entry = input("Please enter the account's PIN: ")
        if status == 'admin':
            if len(pin_entry) == 7:
                try:
                    pin = int(pin_entry)
                    break
                except ValueError:
                    invalid_pin()
            else:
                invalid_pin()
        else:
            if len(pin_entry) == 4:
                try:
                    pin = int(pin_entry)
                    break
                except ValueError:
                    invalid_pin()
            else:
                invalid_pin()
    return pin


def check_admin(username):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM profiles')
        profiles = [{'username': row[0], 'status': row[1], 'pin': row[2]} for row in cursor.fetchall()]

    for profile in profiles:
        if profile['username'] == username and profile['status'] == 'admin':
            return True

    return False


def delete_profile(username):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM profiles WHERE username = ?', (username,))


def profile_count():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT count(*) FROM profiles')


def hard_reset():
    print("In order to proceed we will need to verify that you are the owner of this program.\n")
    attempts = 0
    while attempts <= 3:
        username = input("Please enter your username: ")
        pin = input("Please enter your PIN: ")
        if sign_in(username, pin):
            if check_admin(username):
                database.delete_database()
                return
            else:
                attempts += 1
        else:
            attempts += 1
        print(f"That was incorrect. {3 - attempts} remaining.")
    print('Access denied. Shutting down.')
    raise SystemExit


def invalid_pin():
    print("""\nThat was an invalid input!
    The PIN should only consist of numbers, no letters or special characters.
    Please try again using a valid PIN entry\n""")
