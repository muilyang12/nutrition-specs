import sqlite3

source_conn = sqlite3.connect("./db.sqlite3")
source_cursor = source_conn.cursor()

destination_conn = sqlite3.connect("./be/db.sqlite3")
destination_cursor = destination_conn.cursor()


def print_table_names():
    source_conn.execute("SELECT name FROM sqlite_master WHERE type='table';")

    tables = source_conn.fetchall()

    print("Tables in the database:")
    for table in tables:
        print(table[0])


def migrate_all_data(table_name):
    source_cursor.execute(f"SELECT * FROM {table_name}")
    rows = source_cursor.fetchall()

    for row in rows:
        placeholders = ", ".join(["?"] * len(row))
        destination_cursor.execute(
            f"INSERT INTO {table_name} VALUES ({placeholders})", row
        )
        destination_conn.commit()


migrate_all_data("food_foodcategory")

source_conn.close()
destination_conn.close()
