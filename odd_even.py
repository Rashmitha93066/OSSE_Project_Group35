# Program to check if the input number is odd or even.
# Take your input
# Call the find function
# Print if the number is even or odd
def find(num):
    # code logic here
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

num = int(input('Enter the number: '))  # 
numtype = find(num)                     # 
print('Given number is',numtype).       #  