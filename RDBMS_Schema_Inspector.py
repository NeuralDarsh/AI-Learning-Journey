# Practicing Database Inspection and Python-SQL Integration

import sqlite3

def inspect_database():
    # 1. Connect to our existing bank database (from Day 47)
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    print("---  RDBMS: Database Schema Inspector ---")
    
    try:
        # 2. Query the 'sqlite_master' table (The metadata table)
        # This is a standard way to see all tables in SQLite
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("No tables found in this database.")
            return

        for table_name in tables:
            name = table_name[0]
            print(f"\n[Table: {name}]")
            
            # 3. Use PRAGMA to get column details (Metadata)
            # This shows: (id, name, type, notnull, default_value, pk)
            cursor.execute(f"PRAGMA table_info({name});")
            columns = cursor.fetchall()
            
            print(f"{'ID':<3} | {'Column Name':<15} | {'Type':<10} | {'PK':<3}")
            print("-" * 35)
            for col in columns:
                # col[5] is 1 if it's a Primary Key, else 0
                pk_status = "YES" if col[5] == 1 else "NO"
                print(f"{col[0]:<3} | {col[1]:<15} | {col[2]:<10} | {pk_status:<3}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    inspect_database()