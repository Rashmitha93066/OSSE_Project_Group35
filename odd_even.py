# Program to check if the input number is odd or even.
# Take your input
# Call the find function
def find(num):
    # code logic here
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

num = int(input('Enter the number: '))  # 
numtype = find(num)                     # 2. 
print('Given number is',numtype).       # 3. print if the number is even or odd