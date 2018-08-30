# Ashwin Chidambaram                        ##
# Task: What is the 10001st prime number?   ##
##############################################
# Self assesment on program runtime ##
import time                         ##
start_time = time.time()            ##
######################################

# Create a list to store a list of prime numbers
primeList = [2]
num = 3
i = 2

# Iterate till we have 10001 values
while (len(primeList)) != 10001:

    # Set prime as a check condition. If prime ever becomes False, that number is not prime
    prime = True

    # Create a while loop that will check if a number is divisible by anything other than 1 and itself
    while i != (num - 1):

        # Divide num by value
        val = num % i

        # If there ever comes a situation where the number is divisible by anything, set trigger to False
        if val == 0:
            prime = False
            break      # Break from loop since proved not prime

        # Increment the divisior by 1
        i = i + 1

    # If the prime condition remains True after testing a number, add it to the list
    if prime == True:
        primeList.append(num)

    # Increase the number being tested by 1, and reset the dividing value
    num = num + 1
    i = 2

# End runtime measure
runtime = time.time() - start_time

# Print output
print('The 10001st Prime Number is: {}'.format(primeList.pop()))

# Print runtime
print('RunTime: {} seconds'.format(round(runtime,4)))
