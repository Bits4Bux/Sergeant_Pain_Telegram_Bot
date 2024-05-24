from DataBaseManager import DataBaseManager

"""Adds questions and answers to a SQLite database and displays them"""
db_manager = DataBaseManager()
db_manager.create_table()  # Creates the SQLite database file


def show_qa():  # Retrieve and print all questions and answers
    rows = db_manager.get_all_fragen_antworten()
    for row in rows:
        print(f"ID: {row[0]}, Frage: {row[1]}, Antwort: {row[2]}")


db_manager.insert_frage_antwort("ADD_HERE_QUESTION", "ADD_HERE_ANSWER")  # Insert question and answer

show_qa()  # Comment out if you don't want the questions/answers displayed.
db_manager.close_connection()  # Closes the database connection
