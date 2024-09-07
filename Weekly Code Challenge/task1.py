# Step 1: Initialize an empty list to store integers
integers_list = []

# Step 2: Ask the user how many integers they want to add to the list
num_of_integers = int(input("How many integers would you like to enter? "))

# Step 3: Loop through the number of integers the user wants to input
for i in range(num_of_integers):
    # Prompt the user to enter an integer
    user_input = int(input(f"Enter integer {i+1}: "))
    # Append the entered integer to the list
    integers_list.append(user_input)
    
# Step 4: Compute the sum of all integers in the list
sum_of_integers = sum(integers_list)

# Step 5: Print the sum of the integers
print("The sum of all the integers in the list is:", sum_of_integers)