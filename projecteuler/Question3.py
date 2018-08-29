# Ashwin Chidambaram                                                ##
# Task: What is the largest prime factor of the number 600851475143 ##
######################################################################
import math

# Create a list to hold the factors of 600851475143
factorList = []

# Create a variable to store the number that will be divided into 600851475143 to see if it's a factor
num = 1

# Create a while loop to iterate till it reaches half the value of the original number
while num <= (math.sqrt(13195)):

    # Take the mod of 600851475143 % num and check if = 0. If true, then its a factor. If false, not a factor
    if 13195 % num == 0:

        # Add number to list
        factorList.append(num)
        num += 1

    else:
        num += 1

print(factorList)#############
