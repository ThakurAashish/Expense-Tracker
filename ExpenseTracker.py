import datetime

expenses = []


def add_expense(amount, category, note=""):
    expense = {
        "date": datetime.date.today().isoformat(),
        "amount": amount,
        "category": category,
        "note": note
    }
    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("Date       | Amount | Category | Note")
    print("-------------------------------------")
    for e in expenses:
        print(f"{e['date']} | {e['amount']} | {e['category']} | {e['note']}")
    print()


def total_expense():
    total = sum(e['amount'] for e in expenses)
    print(f"Total Expense: ₹{total}\n")


def main():
    while True:
        print("Simple Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food, Travel, etc.): ")
            note = input("Enter note (optional): ")
            add_expense(amount, category, note)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()