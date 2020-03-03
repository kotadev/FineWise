from utils.databases.database_connection import DatabaseConnection

"""
Concerned with creating, storing, editing, and removing FineWise trackers from table as well as
storing, editing, and removing financial data from their respective trackers
"""


def create_profiles():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        drop_table_statement = 'DROP TABLE IF EXISTS profiles'
        cursor.execute(drop_table_statement)

        print("\nCreating your new FineWise profile now!\n")

        cursor.execute(
            """CREATE TABLE profiles(
            username TEXT PRIMARY KEY,
            status TEXT, 
            pin INTEGER)""")


def create_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('pragma foreign_keys=ON')

        print("\nCreating your new FineWise now.\n")
        table = f"""CREATE TABLE finances(
            profile TEXT, 
            name TEXT,
            category TEXT,
            considered TEXT, 
            amount REAL, 
            start TEXT, 
            frequency TEXT, 
            stop TEXT,
            PRIMARY KEY(profile, name),
            FOREIGN KEY(profile) REFERENCES profiles(username) ON DELETE CASCADE)"""

        cursor.execute(table)


def delete_database():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DROP TABLE IF EXISTS profiles')
        cursor.execute('DROP TABLE IF EXISTS finances')







