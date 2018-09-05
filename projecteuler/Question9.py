# Ashwin Chidambaram                                                                                    ##
# Task: There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc   ##
##########################################################################################################
# Self assesment on program runtime ##
import time                         ##
start_time = time.time()            ##
######################################

# Import math library to be able to take square root
import math

# Declare variables
a = 2               # Value of a
b = 3               # Value of b
c = 4               # Value of c
i = 0               # Counter used to iterate through use cases
sumVal = 1000.0     # Change sumVal to any floating point value

# Declare condition for where program will loop till we get the value we want
while sum != sumVal:

    # Increment a and b by a value of 1 to get set values
    a = a + 1
    b = b + 1

    # Set iteration in 10000 range since there are many possibilities for a triplet
    while i != 10000:

        # Multiply a, b in increments of 10 sp as to not run more than necessary
        sum = (a ** 2) + (b ** 2)

        # Take the root of sum of a^2 and b^2 to get c
        c = math.sqrt(sum)

        # Check if the sum is a perfect square, if not then don't worry about it
        if c.is_integer() == True:

            # Since c is a perfect sqaure, sum (a, b, c) and check if it is 1000
            sum = a + b + c
            #print('SUM: {}'.format(sum))
            #print('C: {}'.format(c))

            # If the sum is equal to 1000, store the values at this point and break loop
            if sum == sumVal:
                A = a
                B = b
                C = c
                break

        # Increment b by 1 and loop count by 1
        b = b + 1
        i = i + 1

    # If loop above has run i times, reset b to the original value so that the next set can be checked and reset the loop counter
    b = b - i
    i = 0

# End runtime measure
runtime = time.time() - start_time

# Print output
print ('Product of abc: {}'.format((A*B*C)))

# Print runtime
print('RunTime: {} seconds'.format(round(runtime,4)))
