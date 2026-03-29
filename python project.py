class Item:
    def __init__(self, item_id, name, location):
        self.item_id = item_id
        self.name = name
        self.location = location

    def display(self):
        print(f"ID: {self.item_id}, Name: {self.name}, Location: {self.location}")

items = []

def add_item():
    item_id = input("Enter Item ID: ").strip()
    name = input("Enter Item Name: ").strip()
    location = input("Enter Lost Location: ").strip()

    if not item_id or not name or not location:
        print("All fields are required!")
        return

    # Check for duplicate IDs
    for item in items:
        if item.item_id == item_id:
            print("Item ID already exists!")
            return

    items.append(Item(item_id, name, location))
    print("Item added successfully!")

def view_items():
    if not items:
        print("No items to display.")
        return
    print("\nLost Items:")
    for item in items:
        item.display()

def search_item():
    search_id = input("Enter Item ID to search: ").strip()
    for item in items:
        if item.item_id == search_id:
            print("Item found:")
            item.display()
            return
    print("Item not found.")

def delete_item():
    delete_id = input("Enter Item ID to delete: ").strip()
    for i, item in enumerate(items):
        if item.item_id == delete_id:
            del items[i]
            print("Item deleted successfully.")
            return
    print("Item not found.")

def menu():
    while True:
        print("\n1. Add Item\n2. View Items\n3. Search Item\n4. Delete Item\n5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            search_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()