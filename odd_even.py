# Program to check if the input number is odd or even.

def find(num):
    # code logic here
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

num = int(input('Enter the number: '))  # 1. take your input
numtype = find(num)                     # 2. call the find function
print('Given number is',numtype).       # 3. print if the number is even or odd