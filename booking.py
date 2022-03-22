import sys

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
    print('test')


def review_bookings():
    print('test')
    
menu()