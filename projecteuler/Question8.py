# Ashwin Chidambaram                                                                                ##
# Task: Find the thirteen adjacent digits in the 1000-digit number that have the greatest product   ##
######################################################################################################
# Self assesment on program runtime ##
import time                         ##
start_time = time.time()            ##
######################################

# Create a list to store the list of products
productList = []

# Input number
number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# Remap the whole number into a list containing each digit as an entity
chars = list(map(int, str(number)))

# Create variables a, b, c
a = 0       # Represents the 0th index and will increment by 1
b = 13      # Represnets the 13th index and will increment by 1
c = a       # Will be used as a replacement for 'a'

product = 1 # This variable will hold the product of the 13 digits

# While we haven't iterated through the entire number
while b != (len(str(number)) + 1):

    # Create ordered pairs with a length of 13 char
    while c != b: #(len(number) + 1)

        # Find the product
        product = product * chars[c]

        # Increment c by 1 so as to cycle the 13 indexes between a and b
        c = c + 1

    # Add the product to the list containing products
    productList.append(product)

    # Prep a, b, and c for next pass
    a = a + 1       # Increment a by 1; ex: 0 -> 1
    b = b + 1       # Increment b by 1; ex: 13 -> 14
    c = a           # Reset c to the new value of a

    product = 1     # Reset product back to 1 so we can get a new product

# Sort the list of products to get the largest one
productList.sort()

# Get largest value
value = productList.pop()

# End runtime measure
runtime = time.time() - start_time

# Print output
print('Greatest Product: {}'.format(value))

# Print runtime
print('RunTime: {} seconds'.format(round(runtime,4)))
