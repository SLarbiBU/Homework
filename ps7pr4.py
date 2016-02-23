#
# ps7pr4.py (Problem Set 7, Problem 4)
#
# TT Securities
#
# Computer Science 111
#
# name:
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the min and its day')
    print('(6) Find the max and its day')
    print('(7) Test a threshold')
    print('(8) Your TT investment plan')
    print('(9) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_list = eval(input('Enter a new list of prices: '))
    return new_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    d = 0
    print('Day',' ', 'Price')
    print('---',' ','-----')
    for x in prices:
            print('  ', d,' ', x)
            d += 1

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

def average_price(prices):
    ''' returns the average price in the list of prices input.
    '''
    total = 0.0
    for x in prices:
        total = total + x

    return total/len(prices)



def standard_deviation(prices):
    sum_diffsquared = 0
    for x in prices:
        diff = x - average_price(prices)
        diffsquared = diff**2
        sum_diffsquared += diffsquared 

        standarddeviation = ((sum_diffsquared)/(len(prices)))**(1/2)

def min_price(prices):
    
    y = prices[0]
    for x in prices:
        diff = x - y
        if diff >= x:
            return x
    print(x)
    
    
## Add your helper functions for options 3-8 below.


def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 9:
            break
        elif choice < 9 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        elif choice == 3:
            average = average_price(prices)
            print('The average price is', average)
        elif choice == 4:
            standarddeviation = standard_deviation(prices)
            print('The standard deviation is', standard_deviation(prices))
        elif choice == 5:
            min_price = min_price(prices)
            print('The min price is', min_price)
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
