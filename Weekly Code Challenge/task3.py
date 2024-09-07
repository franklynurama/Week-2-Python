# Step 1: Create an empty dictionary to store information about the person
person_info = {}

# Step 2: Ask the user for input and store the information in the dictionary
person_info['name'] = input("Enter your name: ")
person_info['age'] = int(input("Enter your age: "))
person_info['favorite_color'] = input("Enter your favorite color: ")

# Step 3: Print the dictionary to the console
print("\nHere is the information you provided:")
print(person_info)