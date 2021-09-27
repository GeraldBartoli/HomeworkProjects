# Ask user for two numbers
num1 = input("What is the first number?")
num2 = input("What is the second number?")

# Create a loop that does the following until the product and sum are the same

# Calculate and display their sum
sum = int(num1) + int(num2)
print(str(sum))

# Calculate and display their product
prod = int(num1) * int(num2)
print(str(prod))

while (sum != prod):
    print("The sum and the product are not equal.")
    num1 = input("What is the first number?")
    num2 = input("What is the second number?")
print("You found the right numbers!")

# If their sum and their product are equal - tell the user
# otherwise ask for two more numbers