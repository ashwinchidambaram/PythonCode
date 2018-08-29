# Ashwin Chidambaram 											                                                                        ##
# Task: Considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms  ##
##########################################################################################################################################

# Create a list that will hold the Fibonacci sequence up to a value of 4,000,000
flist = [1, 2]

# Create a list to hold the even values from flist above
elist = []

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

# Get all the even terms from flist and add it to elist
for num in flist:
    if num % 2 == 0:
        elist.append(num)

# Create variable 'total' to store the sum of elist
total = 0

# Sum elist into variable total
for num in elist:
    total += num

# Print total
print(total)
