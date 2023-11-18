# This code offers functions to compute the sum, product, and mean of integer arrays. It also categorizes positive and negative integers within the array.
# Users can input array size and elements

# Funtion to calculate the sum of elements in the array.
def sum_array(integer_array) :
    s = 0

    for i in range(len(integer_array)):
        s += integer_array[i]

    return s

# Function to calculate the product of elements in the array.
def product_array(integer_array) :
    p = 1

    for i in range(len(integer_array)):
        p *= integer_array[i]

    return p

# Function to calculate the mean (average) of elements in the array.
def mean_array(integer_array) :
    return sum_array(integer_array) / len(integer_array)

# Function to separate positive and negative integers in the array and display them
def sign(integer_array) :
    positive_nums = []
    negative_nums = []

    for i in range(len(integer_array)) :
        if integer_array[i] > 0 :
            positive_nums.append(integer_array[i])

        elif integer_array[i] < 0 :
            negative_nums.append(integer_array[i])

    if positive_nums != [] :
        print(f"- Positive integers in the array are: {positive_nums}")
    else :
        print("- There are no positive integers in the array")

    if negative_nums != [] :
        print(f"- Negative integers in the array are: {negative_nums}")
    else:
        print("- There are no negative integers in the array")      

# Main Program

integer_array = []
size = int(input("Enter the size of the array: "))

# Input integers to fill the array
for i in range(size):
    n = int(input("Enter an integer to fill the array: "))
    integer_array.append(n)

# Display the array
print(f"\n- The array is {integer_array}")

# Perform operations and display results
print(f"\n- The sum of the elements in the array is {sum_array(integer_array)}")
print(f"- The product of the elements in the array is {product_array(integer_array)}")
print(f"- The mean of the elements in the array is {mean_array(integer_array)}")

# Display positive and negative integers in the array
sign(integer_array)
