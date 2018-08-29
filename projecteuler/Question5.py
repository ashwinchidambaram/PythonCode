# Ashwin Chidambaram                                                                                        ##
# Task: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?   ##
##############################################################################################################
# Self assesment on program runtime ##
import time                         ##
start_time = time.time()            ##
######################################

# Set base variables to be used
check = None    # Used to see if the number is divisible
a = 0           # Divisor that will be changing

# Create a while loop that will check if the number is divisible from 1 - 20
while check != True:
    # Declare base value of dividen value
    num = 1         # Dividend value that will go 1-20
    a = a + 1       # Increment a by a value of 1

    # Set divisible to True as a method to make a loop that will work more efficently
    check = True

    # Create a while loop that will loop until num = 20 or divisble becomes False
    while check == True:

        # Divide value by num
        quo = a % num

        # Check if value evendly divides
        if quo != 0:
            check = False

            # If false, break and go to next number
            break

        # Increment number by 1 to get next divisor
        num = num + 1

        # If the condition where the numbers eventually reach 21, that means we've exceed our limit of 20 and break there
        if num == 11:
            break

# End timer
runtime = time.time() - start_time

# Print output
print("Smallest positive number evenly divisible by 1 to 20: {}".format(a))

# Print runtime
print('RunTime: {} seconds'.format(round(runtime,4)))
