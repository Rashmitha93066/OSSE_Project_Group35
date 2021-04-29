# Program to check if the input number is odd or even.
# Take your input
# Call the find function
# Print if the number is even or odd
#def find(num):
#    # code logic here
#    if num%2 == 0:
#        numtype="The number is Even."
#    else:
#        numtype = "The number is Odd"
#    return numtype


def find(num):
# code logic here
    if num==0:
        numtype="Neither even nor odd"
    elif num%2 == 0:
        numtype="The number is Even."
    else:
        numtype = "The number is Odd"
    return numtype