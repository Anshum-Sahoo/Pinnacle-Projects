import calendar
from datetime import datetime


def add_reminder():
    date = input("Enter date (DD-MM-YYYY): ")
    event = input("Enter event: ")

    with open("reminders.txt", "a") as f:
        f.write(f"{date} | {event}\n")

    print("Reminder added successfully!")


def view_reminders():
    try:
        with open("reminders.txt", "r") as f:
            reminders = f.read()

            if reminders.strip() == "":
                print("No reminders found!")
            else:
                print("\n--- Reminders ---")
                print(reminders)

    except FileNotFoundError:
        print("No reminders found!")


def delete_reminder():
    try:
        with open("reminders.txt", "r") as f:
            reminders = f.readlines()

        if not reminders:
            print("No reminders to delete!")
            return

        print("\n--- Reminders ---")
        for i, reminder in enumerate(reminders, start=1):
            print(f"{i}. {reminder.strip()}")

        num = int(input("Enter reminder number to delete: "))

        if 1 <= num <= len(reminders):
            reminders.pop(num - 1)

            with open("reminders.txt", "w") as f:
                f.writelines(reminders)

            print("Reminder deleted successfully!")

        else:
            print("Invalid reminder number!")

    except FileNotFoundError:
        print("No reminders found!")

    except ValueError:
        print("Please enter a valid number!")


def search_reminder():
    keyword = input("Enter keyword to search: ")

    try:
        with open("reminders.txt", "r") as f:
            reminders = f.readlines()

        found = False

        for reminder in reminders:
            if keyword.lower() in reminder.lower():
                print(reminder.strip())
                found = True

        if not found:
            print("No matching reminder found!")

    except FileNotFoundError:
        print("No reminders found!")


def today_reminders():
    today = datetime.now().strftime("%d-%m-%Y")

    try:
        with open("reminders.txt", "r") as f:
            reminders = f.readlines()

        found = False

        print("\nToday's Reminders:")

        for reminder in reminders:
            if today in reminder:
                print(reminder.strip())
                found = True

        if not found:
            print("No reminders for today!")

    except FileNotFoundError:
        print("No reminders found!")


year = int(input("Enter Year: "))
print(calendar.calendar(year))

while True:

    print("\n===== Calendar & Reminder App =====")
    print("1. View Month")
    print("2. Add Reminder")
    print("3. View Reminders")
    print("4. Delete Reminder")
    print("5. Search Reminder")
    print("6. Today's Reminders")
    print("7. Exit")

    choice = input("Choose an option: ")

    match choice:

        case "1":
            try:
                month = int(input("Enter Month (1-12): "))

                if 1 <= month <= 12:
                    print(calendar.month(year, month))
                else:
                    print("Invalid month!")

            except ValueError:
                print("Please enter a valid number!")

        case "2":
            add_reminder()

        case "3":
            view_reminders()

        case "4":
            delete_reminder()

        case "5":
            search_reminder()

        case "6":
            today_reminders()

        case "7":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice!")