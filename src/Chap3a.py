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
• Revisetheprogramtoensurethatinputsareenteredas numeric values. Don’t allow the user to proceed if the value entered is not numeric.
• Createanewversionoftheprogramthatallowsyouto choose feet or meters for your inputs.
• ImplementthisprogramasaGUIprogramthatautomat- ically updates the values when any value changes.
"""

def room_area_calc():
    length_of_room = input("What is the length of the room in feet?")
    width_of_room = input