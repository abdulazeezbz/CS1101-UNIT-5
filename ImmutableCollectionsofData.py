# Create a tuple storing borrower's immutable personal details
borrower_record = ("John Doe", "B1023", "2025-10-15")
print("Borrower record:", borrower_record)

# Attempting to modify an element to test immutability
try:
    borrower_record[1] = "B9999"
except TypeError as error:
    print(f"Modification error caught: {error}")

# Determine the number of fields using len() and display each element using a loop
print(f"Total fields in borrower record: {len(borrower_record)}")
print("Borrower profile fields:")
for field in borrower_record:
    print(f"- {field}")