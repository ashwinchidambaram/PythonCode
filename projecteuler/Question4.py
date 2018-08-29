# Ashwin Chidambaram                                                                ##
# Task: Find the largest palindrome made from the product of two 3-digit numbers    ##
######################################################################################
# Self assesment on program runtime ##
import timeit                       ##
start = timeit.default_timer()      ##
######################################

# Declare variable a and b to represent two 2-digit numbers
a = 999
b = 999

palidromes = []

found = False

# While loop that will multiply a and b and collect all palindromes
while a != 0:

    # Multiply a and b
    product = a * b

    # Convert product to a string
    pstring = str(product)

    # Reverse string so that we can check if palindrome
    rstring = pstring[::-1]

    #print('OG: {} Rev: {}'.format(pstring, rstring))

    # Check if strings are a palindrome. If yes, add it to the list
    if rstring == pstring:
        palidromes.append(product)

    # Decrement b by 1 so as to get the next product
    b = b - 1

    # If b has hit 0, decremnt a by 1 and start the cycle again
    if b == 0:
        a = a - 1
        b = a

# Sort the list of palindromes (will sort from least to greatest)
palidromes.sort()

# End timer
stop = timeit.default_timer()

# Print output message and pop the last value from the list since that is the largest
print('The largest palindrome made from the product of two 3-digit numbers is: {}'.format(palidromes.pop()))

# Print runtime
print('RunTime: {} seconds'.format(round((stop - start),4)))
