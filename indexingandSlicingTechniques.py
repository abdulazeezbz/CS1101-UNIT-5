# Weekly borrowing statistics for consecutive weeks
borrowed_books = [23, 19, 31, 27, 22, 30, 25]
print("Original borrowing statistics:", borrowed_books)

# Extract records from week 2 to week 5 using slicing
# Week 1 is index 0; week 2 is index 1; week 5 corresponds to index 4 (stop at slice index 5)
mid_month_slice = borrowed_books[1:5]
print("Extracted statistics (Week 2 to Week 5):", mid_month_slice)

# Replace the number of books borrowed in week 1 with 20 using indexing
borrowed_books[0] = 20

# Display final results
print("Updated borrowing statistics:", borrowed_books)