import calendar
year = int(input("Enter the year: "))
print(calendar.calendar(year))
while True:
    print("\n1. View Month")
    print("2. Add Reminder")
    print("3. View Reminders")
    print("4. Exit")

    choice = input("Choose: ")

    match choice:
        case "1":
            month = int(input("Enter the month: "))
            print(calendar.month(year, month))
        case "2":
            Reminder=input("Enter Reminder: ")
            with open("reminders.txt","a") as f:
                f.write(Reminder)
        case "3":
            with open("reminders.txt", "r") as file:
                print(file.read())
        case "4":
            break

    