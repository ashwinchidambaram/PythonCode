# Ashwin Chidambaram 											                                                                        ##
# Task: Considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms  ##	                                            ##
##########################################################################################################################################

# Create a list that will hold the Fibonacci sequence up to a value of 4,000,000
flist = [1, 2]

# Create an index variable so we can have a loaction from which to add
index = 1

# Create a sum and allTerms value for data collection and validation
sum = 0
allTerms = False

# Create a while loop to see if all values less than 4,000,000 have been gathered
while allTerms != True:

    # Add last two values and append that to the list
    sum = flist[index] + flist[index-1]

    # Check if value has exceeded 4,000,000
    if sum >= 4000000:
        allTerms = True

    else:
        # Add value to the list
        flist.append(sum)

        # Increase the index value
        index += 1

print(flist)
