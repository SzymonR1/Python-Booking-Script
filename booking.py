import sys, os
os.chdir('Programming-Project')

i = 0

while os.path.exists(f'booking_{i}.txt'):
    i += 1


def menu():
    print('LONG ISLAND HOLIDAYS\n=====================')
    user_input = int(input('1. Make a booking\n2. Review Bookings\n3. Exit\nChoose an option: '))

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
    
    print('LONG ISLAND HOLIDAYS - Making a Booking\n========================================')
    family_name = str(input('Enter your family name: '))
    phone_number = int(input('Enter your phone number: '))
    accommodation_type = int(input('Choose your accommodation type:\n1. Deluxe Caravan (€2000)\n2. Standard Caravan (€1600)\n3. Camp Site (€200)\n4. No Booking\nChoose an option: '))

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
    family_pool_pass = int(input('Do you require a family pool pass?:\n1. Yes\n2. No\nChoose an option: '))

    if family_pool_pass == 1:
        family_pool_pass_cost = 150
        family_pool_pass_name = 'Yes'
    
    if family_pool_pass == 2:
        family_pool_pass_cost = 0
        family_pool_pass_name = 'No'

    kids_amount = int(input('How many kids will join the kids club?: '))

    print('Booking Details\n===============', file=open(f'booking_{i}.txt', 'a'))

    print(f'Surname: {family_name.capitalize()}', file=open(f'booking_{i}.txt', 'a'))
    print(f'Booking ID: {i}', file=open(f'booking_{i}.txt', 'a')) # booking id - not yet implemented - come back later
    print(f'Accommodation Type: {accommodation_type_name}', file=open(f'booking_{i}.txt', 'a'))
    print(f'No. of People: {group_size}', file=open(f'booking_{i}.txt', 'a'))
    print(f'Pool Pass: {family_pool_pass_name}', file=open(f'booking_{i}.txt', 'a'))
    print(f'Kids joining kids club: {kids_amount}', file=open(f'booking_{i}.txt', 'a'))
    print(f'Accommodation cost: {accommodation_cost}', file=open(f'booking_{i}.txt', 'a'))
    print(f'Phone number: {phone_number}', file=open(f'booking_{i}.txt', 'a'))

    total_cost = accommodation_cost + (kids_amount * 100) + family_pool_pass_cost

    print(f'Total cost: {total_cost}', file=open(f'booking_{i}.txt', 'a'))


def review_bookings():
    print('temporary') # work on this - need to implement something similar to Q3 from Week 7 to get this to work

menu()