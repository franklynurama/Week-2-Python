# Step 1: Create a list of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Step 2: Use list comprehension to filter words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Step 3: Print the new list
print(odd_length_words)