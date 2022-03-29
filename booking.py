import sys
import os
os.chdir('Programming-Project')

i = 0


def menu():
    print('LONG ISLAND HOLIDAYS\n=====================')
    user_input = int(
        input('1. Make a booking\n2. Review Bookings\n3. Exit\nChoose an option: '))

    if user_input == 1:
        make_a_booking()

    if user_input == 2:
        review_bookings()

    if user_input == 3:
        sys.exit(0)

    else:
        menu()


def make_a_booking():

    accommodation_cost = 0

    family_pool_pass_cost = 0

    # TODO: - need to append output into text files

    print('LONG ISLAND HOLIDAYS - Making a Booking\n========================================')
    while True:
        surname = str(input('Enter your surname: '))
        if len(surname) >= 15 or len(surname) <= 0:
            print('Enter a valid surname (1-15) characters long.')
            continue
        else:
            break

    while True:
        phone_number = str(input('Enter your phone number: '))
        if len(phone_number) >= 12 or phone_number.isupper() or phone_number.islower():
            print('Phone number is too long, or it contains a letter.')
            continue
        else:
            break


# TODO: LOOP THE REMAINING FUNCTIONS
    accommodation_type = int(input(
        'Choose your accommodation type:\n1. Deluxe Caravan (€2000)\n2. Standard Caravan (€1600)\n3. Camp Site (€200)\n4. No Booking\nChoose an option: '))

    if accommodation_type == 1:
        accommodation_type_name = 'Deluxe'
        accommodation_cost = 2000

    if accommodation_type == 2:
        accommodation_type_name = 'Standard'
        accommodation_cost = 1600

    if accommodation_type == 3:
        accommodation_type_name = 'Camp'
        accommodation_cost = 200

    if accommodation_type == 4:
        sys.exit(0)

    group_size = int(input('How many people in your group?: '))
    family_pool_pass = int(
        input('Do you require a family pool pass?:\n1. Yes\n2. No\nChoose an option: '))

    if family_pool_pass == 1:
        family_pool_pass_cost = 150
        family_pool_pass_name = 'Yes'

    if family_pool_pass == 2:
        family_pool_pass_cost = 0
        family_pool_pass_name = 'No'

    kids_amount = int(input('How many kids will join the kids club?: '))

    total_cost = accommodation_cost + \
        (kids_amount * 100) + family_pool_pass_cost

    file_name = surname + '_'

    print(f'Booking Details\n===============\nSurname: {surname.capitalize()}\nBooking ID: {i}\nAccommodation Type: {accommodation_type_name}\nNo. of People: {group_size}\nPool Pass: {family_pool_pass_name}\nKids joining kids club: {kids_amount}\nPhone number: {phone_number}\nAccommodation cost: {accommodation_cost} EUR\nTotal cost: {total_cost} EUR', file=open(
        f'{file_name+str(i)}.txt', 'a'))


def review_bookings():
    # FIXME: - need to implement something similar to Q3 from Week 7 to get this to work
    input('Test')


menu()
