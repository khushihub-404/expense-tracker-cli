import sqlite3


def add_transaction(date, category, t_type, amount):

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions(date, category, type, amount)
    VALUES (?, ?, ?, ?)
    """, (date, category, t_type, amount))

    conn.commit()
    conn.close()

    print("Transaction Added Successfully!")



def view_transactions():

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")

    data = cursor.fetchall()

    conn.close()

    print("All Transactions:\n")

    if len(data) == 0:
        print("No transactions found")

    else:
        for row in data:
            print(row)