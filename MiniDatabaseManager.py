# Practicing RDBMS concepts using Python's built-in SQLite3

import sqlite3

def setup_database():
    # Connect to database (creates it if it doesn't exist)
    connection = sqlite3.connect("office_data.db")
    cursor = connection.cursor()

    # Create a table (RDBMS Concept: Schema)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            role TEXT,
            language_skill TEXT
        )
    """)
    
    connection.commit()
    return connection

def add_employee(conn, name, role, lang):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, role, language_skill) VALUES (?, ?, ?)", (name, role, lang))
    conn.commit()
    print(f"✅ Added {name} to the database.")

if __name__ == "__main__":
    print("--- 🗄️ SQLite3 Database Manager ---")
    db_conn = setup_database()
    
    # Adding a sample entry matching your profile
    add_employee(db_conn, "Darshan", "AI Developer", "Japanese N5")
    
    # Retrieval (RDBMS Concept: Querying)
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    
    print("\nCurrent Database Entries:")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Role: {row[2]} | Skill: {row[3]}")
    
    db_conn.close()