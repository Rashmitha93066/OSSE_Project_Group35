#include files to be added here
import Calculator
import odd_even

while(True):
    print("Hello User! What would you like to do today? -\n" \
            "1. Calculator\n" \
            "2. Calculate Area of plane figures\n" \
            "3. Raj program\n" \
            "4. Exit\n")
    
    
    # Take input from the user 
    select = int(input("Select operations form 1, 2, 3, 4 : "))
    
    if select == 1:
        calculator()
    
    elif select == 2:
        # Area function
        print("Calculate Shape Area")
        shape_name = input("Enter the name of shape whose area you want to find: ")
        calculate_area(shape_name)
        
    elif select == 3:
        print("Find Odd or Even Number")
        num = int(input('Enter the number: '))
        print(find(num))
        
    elif select == 4:
        quit()
