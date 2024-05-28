from datetime import datetime 

"""
Create a program that determines how many years you have left until retirement and the year you can retire. It should prompt for your current age and the age you want to retire and display the output as shown in the example that follows.
Example Output
       What is your current age? 25
       At what age would you like to retire? 65
       You have 40 years left until you can retire.
       It's 2015, so you can retire in 2055.
Constraints
• Again, be sure to convert the input to numerical data before doing any math.
• Don’t hard-code the current year into your program. Get it from the system time via your programming lan- guage.
"""
def retirement_calculator():
    current_age = input("What is your current age?")
    retirement_age = input("What age would you like to retire?")
    years_left = int(retirement_age)-int(current_age)
    current_year = datetime.today().year
    retirement_year = int(current_year) + years_left
    if years_left < 0:
        print("Bro, you should retire")
    else:

        print(f'You have {years_left} years left until you can retire')
        print(f"It's {current_year}, so you can retire in {retirement_year}")



if __name__ == "__main__":
    retirement_calculator()