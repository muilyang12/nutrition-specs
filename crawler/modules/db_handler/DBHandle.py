import sqlite3


class DBHandle:
    def __init__(self, db_path) -> None:
        self.db_path = db_path

        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def get_table_names(self):
        if not self.cursor:
            raise Exception("Database not connected. Call connect() first.")

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        tables = self.cursor.fetchall()

        return [table[0] for table in tables]

    def get_column_names(self, table_name):
        if not self.cursor:
            raise Exception("Database not connected. Call connect() first.")

        self.cursor.execute(f"PRAGMA table_info({table_name})")

        columns = self.cursor.fetchall()

        return columns

    def get_table_data(self, table_name):
        if not self.cursor:
            raise Exception("Database not connected. Call connect() first.")

        self.cursor.execute(f"SELECT * FROM {table_name}")

        rows = self.cursor.fetchall()

        return rows
