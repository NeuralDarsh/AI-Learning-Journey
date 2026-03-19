# Practice exporting database records for Data Analysis (AI/ML)

import sqlite3
import csv

def export_to_csv(db_name, table_name):
    try:
        # 1. Connect to our existing library or office database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # 2. Fetch all data from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # 3. Get column headers
        column_names = [description[0] for description in cursor.description]

        # 4. Write to a CSV file
        filename = f"{table_name}_backup.csv"
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(column_names) # Write the Header
            writer.writerows(rows)        # Write the Data

        print(f" Success! Data from '{table_name}' exported to {filename}")

    except sqlite3.Error as e:
        print(f" Database Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("--- RDBMS: Data Export Tool ---")
    # We use 'library.db' from Day 37 or 'office_data.db' from Day 34
    db = input("Enter database name (e.g., library.db): ")
    table = input("Enter table name (e.g., books): ")
    
    export_to_csv(db, table)