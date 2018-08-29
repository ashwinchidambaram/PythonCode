# Ashwin Chidambaram                                                                                        ##
# Task: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?   ##
##############################################################################################################
# Self assesment on program runtime ##
import time                         ##
start_time = time.time()            ##
######################################

# Set base variables to be used
check = None    # Used to see if the number is divisible
base = 20
mult = 20       # Divide multiples of 20 by the numbers to see if valid
a = 19           # Divisor that will be changing
b = 1

# Create a while loop that will check if the number is divisible from 20 to 1
while check != True:

    # Check if mult is divisible by a
    value = mult % a
    #print('Main Value: {}, Dividing Value: {}'.format(mult,a))

    # If value is not 0, then it is not evenly divisible
    if value != 0:
        check = False

        # If not divisible, increment by 1 so 20*1 becomes 20*2 etc. and set a back to base value
        b = b + 1
        a = 19

        # Increase multiple value
        mult = base * b

    # If value does evenly divide, check if it does so for the next number until 1
    else:

        # If counter has reached 1, it is divisible (Can be done earlier for sure though)
        if a == 1:
            check = True

        # Decremnt a by 1 so as to divide bt 18, 17, 16, etc. till 1
        else:
            a = a - 1
            #print('Value of a is: {}'.format(a))

# End runtime measure
runtime = time.time() - start_time

# Print output
print("Smallest positive number evenly divisible by 1 to 20: {}".format(mult))

# Print runtime
print('RunTime: {} seconds'.format(round(runtime,4)))
