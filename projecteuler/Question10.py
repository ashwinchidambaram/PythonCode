# Ashwin Chidambaram                                        ##
# Task: Find the sum of all the primes below two million    ##
##############################################################
# Self assesment on program runtime ##
import time                         ##
start_time = time.time()            ##
######################################
import math

# Create variables
num = 2
prime = None
primeList = []

# Define function to check if prime
def CheckIfPrime(num):
    i = 2
    # Get the halfway point of number
    root = math.sqrt(num)

    # Iterate a mod function till the halfway point
    while i <= root:

        # Store the value of num modded with i
        mod = num % i

        if mod == 0:
            prime = False
            return prime
            break

        else:
            i += 1

# Gather all prime numbers below 2,000,000
while num < 2000000:

    # Check if the number is prime
    result = CheckIfPrime(num)

    # If the number is prime, append to list of primes
    if result == None:
        primeList.append(num)

    # Increment number
    num += 1

sum = 0

# Sum all numbers
for value in primeList:
    sum = sum + value

# End runtime measure
runtime = time.time() - start_time

# Print output
print('Sum: {}'.format(sum))

# Print runtime
print('RunTime: {} seconds'.format(round(runtime,4)))
