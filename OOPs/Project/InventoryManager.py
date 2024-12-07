"""
Inventory Manager

Attributes: Inventory (dictionary with item names as keys and quantities as values).

Methods:

Add item: Increase the quantity or add a new item.
Remove item: Decrease the quantity or remove if it reaches zero.

Display inventory: List all items with their quantities.

Objective: Handle data structures (dictionary) with class methods.

"""

class InventoryManager:
    def __init__(self, items=None):
        # Initialize inventory as a dictionary
        self.items = items if items else {}
    
    def add_item(self, name, quantity):
        # Add or update item
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
    
    def remove_item(self, name, quantity):
        # Remove or decrease quantity
        if name in self.items:
            self.items[name] -= quantity
            if self.items[name] <= 0:
                del self.items[name]
        else:
            print(f"Item '{name}' not found in inventory.")
    
    def display_inventory(self):
        # Display all items
        if self.items:
            print("Current Inventory:")
            for item, qty in self.items.items():
                print(f"{item}: {qty}")
        else:
            print("Inventory is empty.")

# Initialize inventory
inventory = InventoryManager({"chips": 10, "bread": 5})

# Add items
inventory.add_item("chips", 5)
inventory.add_item("milk", 2)

# Remove items
inventory.remove_item("bread", 3)
inventory.remove_item("chips", 15)  # This will remove 'chips' entirely

# Display inventory
inventory.display_inventory()
