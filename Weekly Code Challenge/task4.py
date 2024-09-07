# Step 1: Accept user input to create the first set of integers
set1_input = input("Enter integers for the first set, separated by spaces: ")
set1 = set(map(int, set1_input.split()))

# Step 2: Accept user input to create the second set of integers
set2_input = input("Enter integers for the second set, separated by spaces: ")
set2 = set(map(int, set2_input.split()))

# Step 3: Create a new set that contains only the elements common to both sets
common_set = set1.intersection(set2)

# Step 4: Print the sets and the common elements
print(f"\nFirst set: {set1}")
print(f"Second set: {set2}")
print(f"Common elements: {common_set}")