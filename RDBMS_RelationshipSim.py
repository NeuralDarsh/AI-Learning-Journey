# Demonstrating One-to-Many relationships and Foreign Keys

import sqlite3

def run_database_logic():
    # Connect and create cursor
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Enable Foreign Key support in SQLite
    cursor.execute("PRAGMA foreign_keys = ON")

    # 1. Create Authors Table (Parent Table)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )""")

    # 2. Create Books Table (Child Table with Foreign Key)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors (author_id)
    )""")

    # Insert Data
    try:
        cursor.execute("INSERT OR IGNORE INTO authors (author_id, name) VALUES (1, 'Murakami Haruki')")
        cursor.execute("INSERT OR IGNORE INTO books (title, author_id) VALUES ('Norwegian Wood', 1)")
        cursor.execute("INSERT OR IGNORE INTO books (title, author_id) VALUES ('Kafka on the Shore', 1)")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")

    # Query: Joining tables (RDBMS Concept: JOIN)
    print("--- 📚 Library Database: Author & Books ---")
    cursor.execute("""
        SELECT authors.name, books.title 
        FROM authors 
        JOIN books ON authors.author_id = books.author_id
    """)
    
    for row in cursor.fetchall():
        print(f"Author: {row[0]} | Book: {row[1]}")

    conn.close()

if __name__ == "__main__":
    run_database_logic()