"""
Write a program that prompts for two numbers. Print the sum, difference, product, and quotient of those numbers as shown in the example output: Example Output What is the first number? 10 What is the second number? 5 10 + 5 = 15 10 - 5 = 5 10 * 5 = 50 10 / 5 = 2 Constraints • Values coming from users will be strings. Ensure that you convert these values to numbers before doing the math. • Keep the inputs and outputs separate from the numerical conversions and other processing. • Generate a single output statement with line breaks in the appropriate spots.


• Revise the program to ensure that inputs are entered as numeric values. Don’t allow the user to proceed if the value entered is not numeric.
• Don’t allow the user to enter a negative number.

"""

def get_valid_number(prompt):
    try:
        num = int(input(prompt))
        if num < 0:
            print("Negative numbers are not valid. Please try again.")
            return get_valid_number(prompt)
        else:
            return num
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_valid_number(prompt)

def perform_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 
    return addition, subtraction, multiplication, division

def print_results(num1, num2, results):
    addition, subtraction, multiplication, division = results
    output = f"{num1} + {num2} = {addition}\n"
    output += f"{num1} - {num2} = {subtraction}\n"
    output += f"{num1} * {num2} = {multiplication}\n"
    output += f"{num1} / {num2} = {division}"
    print(output)

def main():
    first_number = get_valid_number("What is the first number? ")
    second_number = get_valid_number("What is the second number? ")
    operation_results = perform_operations(first_number, second_number)
    print_results(first_number, second_number, operation_results)

if __name__ == "__main__":
    main()