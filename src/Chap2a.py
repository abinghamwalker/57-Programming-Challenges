"""
So create a program that prompts for your name and prints a greeting using your name.
Example Output
       What is your name? Brian
       Hello, Brian, nice to meet you!

Constraint
• Keep the input, string concatenation, and output separate.


"""
def my_name_is():
    return input("What is your name ?")

def combination_station(name):
    return f'Hello, {name}, nice to meet you'

def ouput_greeting(greeting):
    return greeting


name = my_name_is()
greeting = combination_station(name)
final_greeting = ouput_greeting(greeting)
print(final_greeting)
