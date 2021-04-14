# define a function for calculating
# the area of a shapes
def calculate_area(name):\
    
  # converting all characters
  # into lower cases
  name = name.lower()
    
  # check for the conditions
  if name == "rectangle":
    l = int(input("Enter rectangle's length: "))
    b = int(input("Enter rectangle's breadth: "))
      
    # calculate area of rectangel
    if l>0 and b>0:
      rect_area = l * b
      print(f"The area of rectangle is {rect_area}.")
    else:  
      print("Sorry! Cannot have 0 dimension")
    
  elif name == "square":
    s = int(input("Enter square's side length: "))
        
    # calculate area of square
    if s>0:
      sqt_area = s * s
      print(f"The area of square is {sqt_area}.")
    else:  
      print("Sorry! Cannot have 0 dimension") 

  elif name == "triangle":
    h = int(input("Enter triangle's height length: "))
    b = int(input("Enter triangle's breadth length: "))
        
    # calculate area of triangle
    if b>0 and h>0:
      tri_area = 0.5 * b * h
      print(f"The area of triangle is {tri_area}.")
    else:  
      print("Sorry! Cannot have 0 dimension")
  
  elif name == "circle":
    r = int(input("Enter circle's radius length: "))
    pi = 3.14
          
    # calculate area of circle
    if r>0 :
      circ_area = pi * r * r
      print(f"The area of triangle is {circ_area}.")
    else:  
      print("Sorry! Cannot have 0 dimension")
          
  elif name == 'parallelogram':
    b = int(input("Enter parallelogram's base length: "))
    h = int(input("Enter parallelogram's height length: "))
      
    # calculate area of parallelogram
    if b>0 and h>0:
      para_area = b * h
      print(f"The area of parallelogram is {para_area}.")
    else:  
      print("Sorry! Cannot have 0 dimension")

  elif name == 'trapezoid':
    b1 = int(input("Enter trapezoid's base length 1: "))
    b2 = int(input("Enter trapezoid's base length 2: "))
    h = int(input("Enter trapezoid's height length: "))
      
    # calculate area of trapezoid
    if b1>0 and b2>0 and h>0:
      trape_area = (b1+b2) * 0.5 * h
      print(f"The area of trapezoid is  {trape_area}.") 
    else:  
      print("Sorry! Cannot have 0 dimension")
    
  else:
      print("Sorry! This shape is not available")
