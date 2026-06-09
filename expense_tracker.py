import json
import os

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expenses(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (food, travel, etc.): ")

    if date not in expenses:
        expenses[date] = []

    expenses[date].append({"amount": amount, "category": category})
    save_expenses(expenses)
    print("Expense added successfully!\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return
    for date, items in expenses.items():
        print(f"\nDate: {date}")
        for i, entry in enumerate(items):
            print(f"  [{i}] ₹{entry['amount']} on {entry['category']}")
    print()

def delete_expense(expenses):
    date = input("Enter date to delete from expenses: ")
    if date in expenses:
        view_expenses({date: expenses[date]})
        try:
            index = int(input("Enter index of expense to delete (starting from 0): "))
            del expenses[date][index]
            if not expenses[date]:
                del expenses[date]
            save_expenses(expenses)
            print("Deleted successfully!\n")
        except (ValueError, IndexError):
            print("Invalid index!\n")
    else:
        print("No expenses found for this date.\n")

def main():
    expenses = load_expenses()
    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.\n")

main()