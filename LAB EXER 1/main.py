items = []

while True:
    print("\n1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Remove")
    print("5. Count")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        items.append(item)
        print("Item added.")

    elif choice == "2":
        print("Items:", items)

    elif choice == "3":
        item = input("Search item: ")

        if item in items:
            print("Item found.")
        else:
            print("Item not found.")

    elif choice == "4":
        item = input("Remove item: ")

        if item in items:
            items.remove(item)
            print("Item removed.")
        else:
            print("Item not found.")

    elif choice == "5":
        print("Total items:", len(items))

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
