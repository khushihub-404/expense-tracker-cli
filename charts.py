import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def create_chart():

    conn = sqlite3.connect("expenses.db")

    query = """
    SELECT category, SUM(amount) as total
    FROM transactions
    WHERE type='expense'
    GROUP BY category
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    plt.bar(df["category"], df["total"])

    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.title("Expenses By Category")

    plt.savefig("charts/expense_chart.png")

    print("Chart Saved!")