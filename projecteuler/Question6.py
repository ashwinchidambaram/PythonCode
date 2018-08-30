# Ashwin Chidambaram                                                                                                            ##
# Task: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum   ##
##################################################################################################################################
# Self assesment on program runtime ##
import time                         ##
start_time = time.time()            ##
######################################

# Create a list to contain natural numbers from 1 - 100
nnums = []
sumS = 0
squareS = 0

# Populate the list
i = 0

# Create a while loop to iterate and fill list
while i != 100:

    # Increment i
    i += 1

    # Add i to list
    nnums.append(i)

# Find the sum of the squares and sum of all nums (not squared yet)
for value in nnums:
    sumS = sumS + (value ** 2)
    squareS = squareS + value

# Square sum of all numbers
squareS = squareS ** 2

# End runtime measure
runtime = time.time() - start_time

# Print output
print('The difference is: {}'.format(squareS - sumS))

# Print runtime
print('RunTime: {} seconds'.format(round(runtime,4)))
