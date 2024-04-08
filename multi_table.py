def run():
    print("Generate a new Multiplication Table!")
    integer = int(input("Enter a number (2-20): "))
    validate(integer)


def validate(integer):
    if integer < 2 or integer > 20:
        print("Please enter a number between 2 and 20.")
        integer = int(input("Enter a number (2-20): "))
        validate(integer)
    else:
        total(integer)
        yes() 


def yes():
    yes = input("Would you like to generate another multiplication table? (y/n): ")
    if yes == "y":
        run()
    elif yes == "n":
        print("Goodbye!")
    else:
        print("Please enter 'y' for yes and 'n' for no.")
        yes = input("Would you like to generate another multiplication table? (y/n): ")
        yes()


def total(integer):
    print('  ', end='')
    for j in range(1, integer+1):
        print(j, end='')
    print('  ')

  
    for i in range(1, integer+1, 1):
        print(i, end=' ')
        row_total = 0
        for j in range(1, integer+1):
            row_total += i * j
            print(i * j, end=' ')
        print()
   


run()