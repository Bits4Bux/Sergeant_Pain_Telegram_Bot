import sqlite3
from sqlite3 import Error


class DataBaseManager:
    def __init__(self):
        """Initialize the database manager with the database file path."""
        self.db_file = "sergeant_pain.db"  # Name as you like
        self.connection = self.create_connection()

    def create_connection(self):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            print(f"Connection to SQLite DB successful. SQLite version: {sqlite3.version}")
        except Error as e:
            print(f"Error occurred while connecting to SQLite: {e}")
        return conn

    def create_table(self):
        """Create a table with three columns: id, frage, and antwort."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS fragen_antworten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            frage TEXT NOT NULL,
            antwort TEXT NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Table 'fragen_antworten' created successfully.")
        except Error as e:
            print(f"Error occurred while creating the table: {e}")

    def insert_frage_antwort(self, frage, antwort):
        """Insert a new row into the fragen_antworten table."""
        insert_sql = """
        INSERT INTO fragen_antworten (frage, antwort)
        VALUES (?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (frage, antwort))
            self.connection.commit()
            print("New question and answer inserted successfully.")
        except Error as e:
            print(f"Error occurred while inserting a new row: {e}")

    def get_all_fragen_antworten(self):
        """Retrieve all rows from the fragen_antworten table."""
        select_sql = "SELECT id, frage, antwort FROM fragen_antworten;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error occurred while retrieving rows: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection to SQLite DB closed.")


if __name__ == '__main__':
    pass
