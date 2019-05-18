# Ashwin Chidambaram 											##
# Task: Find the sum of all the multiples of 3 or 5 below 1000	##
##################################################################

# Declare sum and number variables
num = 0
sumValue = 0

# Use while loop to see if we have iterated up to 1000
while num != 1000:

	# Check if num is divisible by 3 or 5
	if (num % 3 == 0) or (num % 5 == 0):
		# Sum value
		sumValue += num

		# Increment value of num
		num += 1

	else:
		# Increment value of num
		num += 1

# Print sum of multiples of 3 or 5 less than 1000
print(sumValue)

 
