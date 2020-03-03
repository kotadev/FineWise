import sqlite3
import menu
from datetime import date
from utils.databases.database_connection import DatabaseConnection
"""
Concerned with initializing FineWise application: (__main__)
"""


def db_exists():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='profiles'")
        if cursor.fetchone()[0] == 1:
            return True
        else:
            return False


def start():
    while True:
        if db_exists():
            profile = menu.main_menu()
        else:
            profile = menu.setup_menu()

        while True:
            if menu.tracker_menu(profile):
                while True:
                    if menu.data_menu(profile):
                        while True:
                            today = date.today()
                            day = int(today.strftime("%d"))
                            month = int(today.strftime("%m"))
                            year = int(today.strftime("%Y"))
                            if not menu.calendar_menu(day, month, year, profile):
                                break
                    else:
                        break
            else:
                break


start()
