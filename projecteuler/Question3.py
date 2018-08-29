# Ashwin Chidambaram                                                ##
# Task: What is the largest prime factor of the number 600851475143 ##
######################################################################
import math

# [1] - Create a list to hold the factors of 600851475143
factorList = []

# Create a variable to store the number that will be divided into 600851475143 to see if it's a factor
num = 2

# [2] - Create a while loop to iterate till it reaches half the value of the original number
while num <= (math.sqrt(600851475143)):

    # Take the mod of 600851475143 % num and check if = 0. If true, then its a factor. If false, not a factor
    if 600851475143 % num == 0:

        # Add number to list
        factorList.append(num)
        num += 1

    else:
        num += 1

# [3] - Check if factor is prime or not
# Set base value of prime to false as a method of check
prime = False

# Create a while loop that will determine the largest prime from the factor list
while prime == False:

    # Get largest factor by popping last value
    factor = factorList.pop()

    # Set divisor to base value of 2
    num = 2

    # Create a while loop to itterate through dividends till it reaches point of x-1, however if a value is triggered by then, break
    while num != factor - 1:
        prime = True

        # Create a variable to store the mod of factor, num
        check = factor % num

        # Check if mod value = 0, since that means their is an even quotient
        if check == 0:
            prime = False
            break   # Break from loop

        # Increment divisor
        num += 1

# Print largest prime value
print('The largest prime factor is: {}'.format(factor))
