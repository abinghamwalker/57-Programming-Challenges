"""
Create a program that calculates the area of a room. Prompt the user for the length and width of the room in feet. Then display the area in both square feet and square meters.
Example Output
       What is the length of the room in feet? 15
       What is the width of the room in feet? 20
       You entered dimensions of 15 feet by 20 feet.
       The area is
       300 square feet
       27.871 square meters
The formula for this conversion is
m2 = f2 × 0.09290304
Constraints
• Keep the calculations separate from the output. • Use a constant to hold the conversion factor.
Challenges
• Revise the program to ensure that inputs are entered as numeric values. Don’t allow the user to proceed if the value entered is not numeric.
• Create a new version of the program that allows you to choose feet or meters for your inputs.
"""

def what_is_the_length() -> int:
    try:
        length = int(input("What is the length of the room in feet?"))
        if length > 0:
            return int(length)
        else:
             print(' Please enter a non negative value for the length:')
             return what_is_the_length()
    except ValueError:
         print("Please enter a valid number:")
         return what_is_the_length()
        
def what_is_the_width() -> int:
    try:
        width = int(input("What is the width of the room in feet?"))
        if width > 0:
            return int(width)
        else:
             print(' Please enter a non negative value for the width:')
             return what_is_the_width()
    except ValueError:
         print("Please enter a valid number:")
         return what_is_the_width()

def area_calc(length,width):
     unit = input('Please enter the unit that you wish to use for area 1) metres or 2)feet:')
     metres_conversion_num =  0.09290304
     print(f'You entered dimensions of {length} feet by {width} feet.')
     area_feet = length * width
     area_metres = area_feet * metres_conversion_num
     if unit == "2":
         print(f'The area is {area_feet} square feet')
     if unit == "1":
         print(f'The area is {area_metres} square metres')
         
    
    

length = what_is_the_length()
width = what_is_the_width()

area_calc = area_calc(length,width)





