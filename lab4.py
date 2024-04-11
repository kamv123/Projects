
def create_phonebook(file):
    phonebook = {}
    for char in file:
        name, phone, address = char.strip('\n').split(',')
        first_name, last_name = name.split()
        phonebook[first_name + ' ' + last_name] = [phone, address]
    return phonebook


def search_phonebook(name, phonebook):
    if name in phonebook:
        print(f'Name: {name}')
        print('Phone number:', phonebook[name][0])
        print('Address:', phonebook[name][1])
    else:
        print('Contact not found.')


def main():
    with open('phonebook.txt') as file:
    	phonebook = create_phonebook(file)
    while True:
        name = input('Enter name to search: ')
        search_phonebook(name, phonebook)
        again = input('Search again (y/n)? ')
        print()
        if again.lower() != 'y':
            print('Goodbye!')
            break

main()

