from utils.databases.database_connection import DatabaseConnection


def add_data(profile, name, category, considered, amount, start, frequency, stop):
    values = (profile, name, category, considered, amount, start, frequency, stop)
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('pragma foreign_keys=ON')

        cursor.execute(f'INSERT INTO finances VALUES(?, ?, ?, ?, ?, ?, ?, ?)', values)


def get_finance_data(profile):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('pragma foreign_keys=ON')

        cursor.execute(f'SELECT * FROM finances WHERE profile = ?', (profile,))
        finance_data = [{'profile': row[0],
                         'name': row[1],
                         'category': row[2],
                         'considered': row[3],
                         'amount': row[4],
                         'start': row[5],
                         'frequency': row[6],
                         'stop': row[7]} for row in cursor.fetchall()]

        return finance_data


def display_data(data):
    print(f"""Name: {data['name']} | Category: {data['category']} |
Considered: {data['considered']} | Amount: {data['amount']} |
Start Date: {data['start']} | Frequency: {data['frequency']} | Stop Date: {data['stop']} |""")


def view_data(profile):
    finance_data = get_finance_data(profile)
    for data in finance_data:
        display_data(data)


def delete_data(profile, name):
    values = (profile, name)
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM finances WHERE profile = ? AND name = ?', values)


def reset_tracker(profile):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM finances WHERE profile = ?', (profile,))


def check_for_category(profile, category):
    values = (profile, category)
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT title FROM finances WHERE profile = ? AND category = ?', values)
        data = cursor.fetchone()

    if data is None:
        return False
    else:
        return True


def check_for_title(profile, name):
    values = (profile, name)
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT name FROM finances WHERE profile = ? AND name = ?', values)
        data = cursor.fetchone()

    if data is None:
        return False
    else:
        return True
