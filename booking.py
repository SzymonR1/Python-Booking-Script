import sys
import os
os.chdir('Programming-Project')


def read_data():
    accommodation = []
    prices = []
    bookings = []
    for line in open('Bookings_2022.txt', 'r'):
        item_in_line = line.strip().split(',')
        accommodation.append(item_in_line[0])
        prices.append(item_in_line[1])
        bookings.append(int(item_in_line[2]))

    return accommodation, prices, bookings


def read_extras():
    extras_read = open('Extras.txt', 'r')
    lines = extras_read.readlines()

    kids_camp_line = lines[0].split(',')
    pool_pass_line = lines[1].split(',')

    kids_camp = int(kids_camp_line[1])
    pool_pass = int(pool_pass_line[1])

    return kids_camp, pool_pass


def write_data(accommodation, prices, bookings):
    bookings_write = open("Bookings_2022.txt", "w")

    for i, items in enumerate(accommodation):
        bookings_write.write(
            f"{accommodation[i]},{prices[i]},{bookings[i]}\n")
    bookings_write.close()


def write_extras(kids_camp, pool_pass):
    extras_write = open("extras.txt", "w")

    extras_write.write(f"Kids Camp,{kids_camp}\nPool Pass,{pool_pass}")
    extras_write.close()


def menu():
    print('LONG ISLAND HOLIDAYS\n=====================')

    while True:
        try:
            user_input = int(
                input('1. Make a booking\n2. Review Bookings\n3. Exit\nChoose an option: '))

            if user_input > 3 or user_input < 0:
                print('Enter a valid option (1-3)')
                continue

            if user_input == 1:
                accommodation, prices, bookings = read_data()
                kids_camp, pool_pass = read_extras()
                make_a_booking(accommodation, prices,
                               bookings, kids_camp, pool_pass)

            if user_input == 2:
                review_bookings()

            if user_input == 3:
                sys.exit(0)

        except ValueError:
            print('Enter a valid option (1-3)')


def make_a_booking(accommodation, prices, bookings, kids_camp, pool_pass):

    i = 1 + bookings[0] + bookings[1] + bookings[2]

    accommodation_cost = 0

    family_pool_pass_cost = 0

    print('LONG ISLAND HOLIDAYS - Making a Booking\n========================================')

    while True:
        surname = str(input('Enter your surname: '))
        if len(surname) >= 15 or len(surname) <= 0:
            print('Enter a valid surname (1-15) characters long.')
            continue
        if not surname.isalpha():
            print('Your surname cannot contain numbers.')
            continue
        else:
            break

    while True:
        phone_number = str(input('Enter your phone number: '))
        if len(phone_number) >= 12 or len(phone_number) <= 0 or phone_number.isupper() or phone_number.islower():
            print('Phone number is too long, or it contains a letter.')
            continue
        else:
            break

    while True:
        try:
            accommodation_type = int(input(
                'Choose your accommodation type:\n1. Deluxe Caravan (€2000)\n2. Standard Caravan (€1600)\n3. Camp Site (€200)\n4. No Booking\nChoose an option: '))

            if accommodation_type > 4 or accommodation_type < 0:
                print('Enter a valid option (1-4)')
                continue

            if accommodation_type == 1:
                accommodation_type_name = 'Deluxe'
                accommodation_cost = 2000
                bookings[0] = bookings[0] + 1
                break

            if accommodation_type == 2:
                accommodation_type_name = 'Standard'
                accommodation_cost = 1600
                bookings[1] = bookings[1] + 1
                break

            if accommodation_type == 3:
                accommodation_type_name = 'Camp'
                accommodation_cost = 200
                bookings[2] = bookings[2] + 1
                break

            if accommodation_type == 4:
                sys.exit(0)

        except ValueError:
            print('Enter a valid input (1-4)')

    while True:
        try:
            group_size = int(input('How many people in your group?: '))
            if group_size > 10:
                print(
                    'If you\'re booking for a group of 10 or more people, please contact us.')
                continue
            if group_size <= 0:
                print('Enter a valid amount (1-10): ')
                continue

        except ValueError:
            print('This input has to be a number.')

        else:
            break

    while True:
        try:
            family_pool_pass = int(
                input('Do you require a family pool pass?: \n1. Yes\n2. No\nChoose an option: '))

            if family_pool_pass == 1:
                family_pool_pass_cost = 150
                family_pool_pass_name = 'Yes'
                pool_pass = pool_pass + 1
                break

            if family_pool_pass == 2:
                family_pool_pass_cost = 0
                family_pool_pass_name = 'No'
                break

        except ValueError:
            print('Enter a valid option (1-2)')

        else:
            continue

    while True:
        try:
            kids_amount = int(
                input('How many kids will join the kids club?: '))
            if kids_amount >= group_size:
                print(
                    'The number of kids cannot be greater than the amount of people in your group.')
                continue
            if kids_amount < 0:
                print('The number of kids cannot be negative.')
                continue

        except ValueError:
            print('Enter a valid number.')

        else:
            kids_camp = kids_camp + kids_amount
            break

    total_cost = accommodation_cost + \
        (kids_amount * 100) + family_pool_pass_cost

    file_name = surname + '_'

    print(f'Booking Details\n===============\nSurname: {surname.capitalize()}\nBooking ID: {i}\nAccommodation type: {accommodation_type_name}\nNo. of people: {group_size}\nPool Pass: {family_pool_pass_name}\nKids joining kids club: {kids_amount}\nPhone number: {phone_number}\nAccommodation cost: {accommodation_cost} EUR\nTotal cost: {total_cost} EUR', file=open(
        f'{file_name}{i:02}.txt', 'a'))

    write_data(accommodation, prices, bookings)
    write_extras(kids_camp, pool_pass)


def review_bookings():
    # TODO: - need to implement something similar to Q3 from Week 7 to get this to work
    print('LONG ISLAND HOLIDAYS - Review Bookings\n=======================================')
    print(f'Deluxe Caravan: ')
    print(f'Standard Caravan: ')
    print(f'Camp Site: ')
    print('')  # blank line spacer
    print(f'Total no. of Pool Passes: ')
    print(f'Total no. of Kids joining Kids Club: ')
    print(f'Most popular accomodation: ')
    print(f'Excpected income: ')
    print(f'Average per booking: ')
    print(f'Number of remaining sites: ')


def main():
    menu()


main()
