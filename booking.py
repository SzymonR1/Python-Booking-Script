import sys # might remove - still testing
import os

i = 0

while os.path.exists(f"file_{i}.dat"):
    i += 1


def menu():
    print('LONG ISLAND HOLIDAYS\n=====================')
    user_input = int(input('1. Make a booking\n2. Review Bookings\n3. Exit\nChoose an option: '))

    if user_input == 1:
        make_a_booking()

    if user_input == 2:
        review_bookings()

    if user_input == 3:
        sys.exit(0) # imported - still testing


def make_a_booking():

    accommodation_cost = 0

    family_pool_pass_cost = 0
    
    print('LONG ISLAND HOLIDAYS - Making a Booking\n========================================')
    family_name = str(input('Enter your family name: '))
    phone_number = int(input('Enter your phone number: '))
    accommodation_type = int(input('Choose your accommodation type:\n1. Deluxe Caravan\n2. Standard Caravan\n3. Camp Site\n4. No Booking\nChoose an option: '))

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
        sys.exit(0) # imported - still testing

    group_size = int(input('How many people in your group?: '))
    family_pool_pass = int(input('Do you require a family pool pass?:\n1. Yes\n2. No\nChoose an option: '))

    if family_pool_pass == 1:
        family_pool_pass_cost = 150
        family_pool_pass_name = 'Yes'
    
    if family_pool_pass == 2:
        family_pool_pass_cost = 0
        family_pool_pass_name = 'No'

    kids_amount = int(input('How many kids will join the kids club?: '))

    print('Booking Details\n===============', file=open(f"file_{i}.dat", "a"))

    print(f'Surname: {family_name.capitalize()}', file=open(f"file_{i}.dat", "a"))
    print('Booking ID: ', file=open(f"file_{i}.dat", "a")) # booking id - not yet implemented - come back later
    print(f'Accommodation Type: {accommodation_type_name}', file=open(f"file_{i}.dat", "a"))
    print(f'No. of People: {group_size}', file=open(f"file_{i}.dat", "a"))
    print(f'Pool Pass: {family_pool_pass_name}', file=open(f"file_{i}.dat", "a"))
    print(f'No. for kids club: {kids_amount}', file=open(f"file_{i}.dat", "a"))
    print(f'Accommodation cost: {accommodation_cost}', file=open(f"file_{i}.dat", "a"))

    total_cost = accommodation_cost + (kids_amount * 100) + family_pool_pass_cost

    print(f'Total cost: {total_cost}', file=open(f"file_{i}.dat", "a"))


def review_bookings():
    print('LONG ISLAND HOLIDAYS - Review Bookings\n======================================')
    print(f'Deluxe Caravan: ')
    print(f'Standard Caravan: ')
    print(f'Camp Site: \n')
    print(f'Total no. of pool passes: ')
    print(f'No. for kids club: ')
    print(f'Most popular accommodation: ')
    print(f'Expected income: ')
    print(f'Average per booking: ')
    print(f'Number of remaining sites: ')

menu()