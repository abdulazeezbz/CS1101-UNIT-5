# Initialize the initial collection of library book titles
book_inventory = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]
print("Initial book inventory:", book_inventory)

# Add two new acquisitions to the list using append()
book_inventory.append("To Kill a Mockingbird")
book_inventory.append("The Great Gatsby")
print("Inventory after additions:", book_inventory)

# Remove a damaged book using remove()
book_inventory.remove("Moby Dick")
print("Inventory after removing damaged book:", book_inventory)

# Sort the inventory in alphabetical order and display the final list
book_inventory.sort()
print("Final alphabetically sorted inventory:", book_inventory)