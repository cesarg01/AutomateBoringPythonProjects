# This program take any natural number n. If n is even, divide it by 2 to get n/2, 
# if n is odd multiply it by 3 and add 1 to obtain 3n+1. Repeat the process indefinitely. 
# The conjecture is that no matter what number you start with, you will always eventually reach 1.
# This is known as the Collatz conjecture.


def collatz(number):
    """
    # Take the user's input and apply the Collatz conjecture 
    """
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

# Keep asking the user for a natural number until they input a natural number.
while True:
    try:
        user_input = int(input('Please enter a number: \n'))
        break
    except ValueError:
        print('Error: Enter a integer')
# Save the first collatz value
value = collatz(user_input)

# Keep calling collatz() until value becomes 1
while value != 1:
    value = collatz(value)
