import math
"""
Write a program to evenly divide pizzas. Prompt for the number of people, the number of pizzas, and the number of slices per pizza. Ensure that the number of pieces comes out even. Display the number of pieces of pizza each person should get. If there are leftovers, show the number of leftover pieces.
Example Output
       How many people? 8
       How many pizzas do you have? 2
       8 people with 2 pizzas
       Each person gets 2 pieces of pizza.
       There are 0 leftover pieces.
Challenges
• Revise the program to ensure that inputs are entered as numeric values. Don’t allow the user to proceed if the value entered is not numeric.
• Alter the output so it handles pluralization properly, for example:
Each person gets 2 pieces of pizza. or
Each person gets 1 piece of pizza.
Handle the output for leftover pieces appropriately as well."""

def input_people():
    people = input("How many people are in your pizza party?")
    return int(people)

def num_of_pizzas():
    pizzas = input("How many pizzas do you have?")
    return int(pizzas)

def pizza_division(people, pizzas):
    pizza_div = (pizzas * 8) / people
    whole_slice = math.floor(pizza_div)
    if whole_slice== 1:
        print(f'Each person gets {whole_slice} piece of pizza.')
    else:
        print(f'Each person gets {whole_slice} pieces of pizza.')

    leftovers = (pizzas * 8) - (people * whole_slice)
    print(f'THere are {leftovers} leftover pieces.')

people = input_people()
pizzas = num_of_pizzas()
div = pizza_division(people,pizzas)
