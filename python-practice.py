# Get user input
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# Check age and print appropriate message
if age >= 18:
    print(f"Hello {name}, you are over 18 years old.")
else:
    print(f"Hello {name}, you are under 18 years old.")