import random
#binary conversion practice
def concatenate_list(lst):
    result = ""
    for i in lst:
        result += str(i)
    return result

def check_decimal(binary_number, decimal_number):
    decimal = 0
    for i in range(len(binary_number)):
        decimal += int(binary_number[i]) * 2 ** (len(binary_number) - i - 1)
    return decimal == decimal_number

rounds = 0
correct = 0

while True:
    rounds += 1
    # Generate a random 5-digit binary number
    binary = concatenate_list([str(random.randint(0, 1)) for i in range(5)])

    # Convert the binary number to decimal
    decimal = int(binary)

    # Ask the user to enter the decimal equivalent of the binary number
    user_input = int(input(f"What is the decimal equivalent of {binary}? "))

    # Check if the user's answer is correct
    if check_decimal(binary, user_input):
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect!")

    # Ask the user if they want to continue or quit
    user_choice = input("Enter 'exit' to quit. Enter anything else to play again: ")
    if user_choice == "exit":
        print(f"In {rounds} rounds, you answered {correct} questions correctly. Thanks for playing!")
        break

