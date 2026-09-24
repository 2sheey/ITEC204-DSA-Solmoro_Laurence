tickets = [
    ["INC1392939", "BOT-Inventory", "Failed to generate the daily report"],
    ["INC1392940", "BOT-Email", "Failed to send the scheduled notification"],
    ["INC1392941", "BOT-DataSync", "Encountered an error during data transfer"],
    ["INC1392942", "BOT-Invoice", "Failed to process an invoice"],
    ["INC1392943", "BOT-Report", "Failed to generate the weekly report"],
    ["INC1392944", "BOT-FileTransfer", "Failed to upload the required file"],
    ["INC1392945", "BOT-DataEntry", "Encountered an error while entering records"],
    ["INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"],
    ["INC1392947", "BOT-Validation", "Failed to validate the submitted records"],
    ["INC1392948", "BOT-Notification", "Failed to send the system alert"]
]


while True:
    print("\n===== INCIDENT TICKET SYSTEM =====")
    print("1. Add Ticket")
    print("2. Display Tickets")
    print("3. Search Ticket")
    print("4. Remove Ticket")
    print("5. Count Tickets")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        id = input("Enter Incident ID: ")
        bot = input("Enter Bot: ")
        description = input("Enter Short Description: ")

        tickets.append([id, bot, description])
        print("Ticket added successfully!")

    elif choice == "2":
        print("\n--- INCIDENT TICKETS ---")

        for ticket in tickets:
            print("ID:", ticket[0])
            print("Bot:", ticket[1])
            print("Description:", ticket[2])
            print()

    elif choice == "3":
        id = input("Enter Incident ID: ")
        found = False

        for ticket in tickets:
            if ticket[0] == id:
                print("\nTicket Found!")
                print("ID:", ticket[0])
                print("Bot:", ticket[1])
                print("Description:", ticket[2])
                found = True

        if not found:
            print("Ticket not found.")

    elif choice == "4":
        id = input("Enter Incident ID to remove: ")
        found = False

        for ticket in tickets:
            if ticket[0] == id:
                tickets.remove(ticket)
                print("Ticket removed successfully!")
                found = True
                break

        if not found:
            print("Ticket not found.")

    elif choice == "5":
        print("Total active tickets:", len(tickets))

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
