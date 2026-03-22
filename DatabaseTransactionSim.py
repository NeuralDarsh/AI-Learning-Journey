# Practicing "Commit" and "Rollback" for data integrity

import sqlite3

def perform_transfer(sender_id, receiver_id, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, name TEXT, balance REAL)")
    cursor.execute("INSERT OR IGNORE INTO accounts VALUES (1, 'Darshan', 5000.0), (2, 'Receiver', 1000.0)")
    conn.commit()

    try:
        print(f"---  Initiating Transfer: {amount} ---")
        
        # 1. Deduct from Sender
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, sender_id))
        
        # Simulating a potential error (uncomment next line to test Rollback)
        # raise ValueError("Network Connection Lost!") 

        # 2. Add to Receiver
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, receiver_id))

        # 3. Finalize the transaction
        conn.commit()
        print(" Transaction Successful: Database Updated.")

    except Exception as e:
        # If ANY step fails, we undo everything
        conn.rollback()
        print(f" Transaction Failed: {e}. All changes rolled back.")

    finally:
        cursor.execute("SELECT * FROM accounts")
        print("\nCurrent Balances:", cursor.fetchall())
        conn.close()

if __name__ == "__main__":
    perform_transfer(1, 2, 1500.0)