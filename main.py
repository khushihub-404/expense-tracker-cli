from tracker import add_transaction
from tracker import view_transactions

from reports import monthly_summary
from reports import export_excel
from reports import export_csv

from charts import create_chart


while True:

    print("\n===== Expense Tracker =====")

    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Monthly Summary")
    print("4. Export Excel")
    print("5. Export CSV")
    print("6. Create Chart")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        date = input("Enter Date (YYYY-MM-DD): ")
        category = input("Enter Category: ")
        t_type = input("income/expense: ")
        amount = float(input("Enter Amount: "))

        add_transaction(
            date,
            category,
            t_type,
            amount
        )

    elif choice == "2":
        view_transactions()

    elif choice == "3":
        monthly_summary()

    elif choice == "4":
        export_excel()

    elif choice == "5":
        export_csv()

    elif choice == "6":
        create_chart()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")