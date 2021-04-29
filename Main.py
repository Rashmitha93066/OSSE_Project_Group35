#include files to be added here
import Calculator
import odd_even 
import Area

while(True):
    print("Hello User! What would you like to do today? -\n" \
            "1. Calculator\n" \
            "2. Calculate Area of plane figures\n" \
            "3. Find Odd even number\n" \
            "4. Exit\n")
    
    
    # Take input from the user 
    select = int(input("Select operations form 1, 2, 3, 4 : "))
    
    if select == 1:
        Calculator.calculator()
    
    elif select == 2:
        # Area function
        print("Calculate Shape Area")
        shape_name = input("Enter the name of shape whose area you want to find: ")
        Area.calculate_area(shape_name)
        
    elif select == 3:
        a = input('Enter the number: ')
        if a.isnumeric():
           b=int(a)
           res=odd_even.find(b)
           print(res)
        else:
           print("please enter numeric data")
        
    elif select == 4:
        quit()
