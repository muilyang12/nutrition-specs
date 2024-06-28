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


def migrate_all_data(table_name, is_with_id_reset=None):
    source_cursor.execute(f"SELECT * FROM {table_name}")
    rows = source_cursor.fetchall()

    if is_with_id_reset:
        for index, row in enumerate(rows):
            temp_list = list(row)
            temp_list[0] = index + 1
            new_row = tuple(temp_list)

            placeholders = ", ".join(["?"] * len(new_row))
            destination_cursor.execute(
                f"INSERT INTO {table_name} VALUES ({placeholders})", new_row
            )
            destination_conn.commit()

    else:
        for row in rows:
            placeholders = ", ".join(["?"] * len(row))
            destination_cursor.execute(
                f"INSERT INTO {table_name} VALUES ({placeholders})", row
            )
            destination_conn.commit()


migrate_all_data("food_foodcategory", True)

source_conn.close()
destination_conn.close()
