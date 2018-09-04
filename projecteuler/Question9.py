# Ashwin Chidambaram                                                                                    ##
# Task: There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc   ##
##########################################################################################################
# Self assesment on program runtime ##
import time                         ##
start_time = time.time()            ##
######################################
# a < b < c
# a^2 + b^2 = c^2
# Make a = 1, b = 2, run b till 11. check. run a = 2, b till 11. repeat till a = 10, b = 11 the move onto next increment
x = 1
tripleList = []
a = None
b = None
c = None
sum = 0

# Multiply a, b and store into a list
while sum <= 1000:

    # Get values of a, b, c
    a = (2 * x) + 1
    b = (2 * (x ** x)) + (2 * x)
    c = (2 * (x ** x)) + (2 * x) + 1

    x = x + 1

    sum = a + b + c

    print('A: {}, B: {}, C: {}, Sum: {}'.format(a,b,c,sum))

for (a,b,c) in tripleList




# End runtime measure
runtime = time.time() - start_time

# Print output
print ('Got it')

# Print runtime
print('RunTime: {} seconds'.format(round(runtime,4)))
