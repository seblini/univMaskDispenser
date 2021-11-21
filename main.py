from person import Person
import os

def main():
    dummy = Person('dummy', '5000000', 0, 0)
    ls = []
    ls.append(dummy)
    home(ls)

def home(ls):
    cls()
    print('PROTECTION KIT VENDING MACHINE')
    print('Welcome! Please login using your name and ticket ID.')
    user_name = input('Name: ')
    user_id = input('Ticket ID: ')
    print_account_information(ls, ls[insertList(ls, user_name, user_id)])

def print_account_information(ls, person):
    cls()
    print('Account Information\n')
    print(f'Name: {person.name}')
    print(f'Ticket ID: {person.ticket_id}')
    print(f'Masks remaining this week: {person.num_masks}')
    print(f'Account Balance: {person.account_balance}\n')
    print('Type 1 to add funds, 2 to purchase mask, 3 to logout')
    user = input()
    if user == '1':
        user = input('Enter amount: ')
        person.add_funds(int(user))
        print_account_information(ls, person)
    elif user == '2':
        print('Type 1 to purchase a face shield, 2 for a regular mask')
        user = input()
        person.get_mask('regular' if user == '2' else 'faceshield')
        print_account_information(ls, person)
    elif user == '3':
        home(ls)

def insertList(ls, name, id):
    for i in range(0, len(ls)):
        if ls[i].name == name and ls[i].ticket_id == id:
            return i
    ls.append(Person(name, id, 7, 0))
    return len(ls)-1

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()

