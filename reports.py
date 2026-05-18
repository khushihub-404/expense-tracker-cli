import sqlite3
import pandas as pd


def monthly_summary():

    conn = sqlite3.connect("expenses.db")

    query = """
    SELECT type, SUM(amount)
    FROM transactions
    GROUP BY type
    """

    df = pd.read_sql_query(query, conn)

    print(df)

    conn.close()



def export_excel():

    conn = sqlite3.connect("expenses.db")

    df = pd.read_sql_query(
        "SELECT * FROM transactions",
        conn
    )

    df.to_excel("exports/report.xlsx", index=False)

    conn.close()

    print("Excel Exported!")



def export_csv():

    conn = sqlite3.connect("expenses.db")

    df = pd.read_sql_query(
        "SELECT * FROM transactions",
        conn
    )

    df.to_csv("exports/report.csv", index=False)

    conn.close()

    print("CSV Exported!")