import sys # might remove - still testing


def menu():
    print('LONG ISLAND HOLIDAYS\n=====================')
    print('1. Make a booking\n2. Review Bookings\n3. Exit\n')
    user_input = int(input('Choose an option: '))

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
        accommodation_type_name = "Deluxe"
        accommodation_cost = 2000

    if accommodation_type == 2:
        accommodation_type_name = "Standard"
        accommodation_cost = 1600

    if accommodation_type == 3:
        accommodation_type_name = "Camp"
        accommodation_cost = 200

    if accommodation_type == 4:
        sys.exit(0) # imported - still testing

    group_size = int(input('How many people in your group?: '))
    family_pool_pass = str(input('Do you require a family pool pass? (Y/N): ')) # CHANGE TO 1 = YES 2 = NO (THAT IS CLEANER)

    if family_pool_pass == 'Y':
        family_pool_pass_cost = 100
    
    if family_pool_pass == 'N':
        family_pool_pass_cost = 0

    kids_amount = int(input('How many kids will join the kids club?: '))

    print('Booking Details\n================')

    print(f'Name: {family_name.capitalize()}')
    print('Booking ID: ') # not yet implemented - come back later
    print(f'Accommodation Type: {accommodation_type_name}')
    print(f'No. of People: {group_size}')
    print(f'Pool Pass: {family_pool_pass}')
    print(f'No. for kids club: {kids_amount}')
    print(f'Cost of accommodation: {accommodation_cost}')

    total_cost = accommodation_cost + (kids_amount * 100) + family_pool_pass_cost

    print(f'Total cost: {total_cost}')



def review_bookings():
    print('test')

menu()